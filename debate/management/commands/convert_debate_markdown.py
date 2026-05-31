import re
from typing import Tuple

from django.core.management.base import BaseCommand
from django.db import transaction

from debate.models import DebateArticle


def _normalize_whitespace(text: str) -> str:
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _ensure_top_heading(article_text: str, sub_topic: str) -> Tuple[str, bool]:
    text = article_text.strip()
    if not text:
        return text, False

    has_heading = bool(re.search(r"(^|\n)\s*#{1,6}\s+", text, flags=re.M))
    if has_heading:
        return text, False

    heading_source = (sub_topic or "").strip()
    if not heading_source:
        heading_source = "Debate Article"

    return f"# {heading_source}\n\n{text}", True


def _decorate_structure(article_text: str) -> Tuple[str, bool]:
    lines = article_text.split("\n")
    out = []
    changed = False

    numbered_section_re = re.compile(r"^\s*(\d+)\.\s+(.+)$")
    label_line_re = re.compile(r"^\s*([\w\- ]{1,50}:)\s*$", flags=re.UNICODE)

    for line in lines:
        stripped = line.strip()

        if not stripped:
            out.append("")
            continue

        if re.match(r"^#{1,6}\s+", stripped):
            out.append(stripped)
            continue

        m_num = numbered_section_re.match(stripped)
        if m_num:
            out.append(f"## {m_num.group(1)}. {m_num.group(2).strip()}")
            if stripped != out[-1]:
                changed = True
            continue

        m_label = label_line_re.match(stripped)
        if m_label and not stripped.lower().startswith(("http:", "https:")):
            out.append(f"### {m_label.group(1)}")
            if stripped != out[-1]:
                changed = True
            continue

        out.append(stripped)

    rebuilt = "\n".join(out)
    rebuilt = re.sub(r"\n{3,}", "\n\n", rebuilt).strip()
    return rebuilt, changed or (rebuilt != article_text)


def _decorate_inline_labels(article_text: str) -> Tuple[str, bool]:
    lines = article_text.split("\n")
    out = []
    changed = False

    label_with_body_re = re.compile(
        r"^\s*(Claim|Correction|Objection|Response|Conclusion|Answer|Question|Principle|Lesson|Theme)\s*:\s*(.+)\s*$",
        flags=re.IGNORECASE,
    )

    for line in lines:
        stripped = line.strip()
        m = label_with_body_re.match(stripped)
        if not m:
            out.append(stripped)
            continue

        label = m.group(1)
        body = m.group(2)
        new_line = f"**{label}:** {body}"
        out.append(new_line)
        if new_line != stripped:
            changed = True

    rebuilt = "\n".join(out)
    rebuilt = re.sub(r"\n{3,}", "\n\n", rebuilt).strip()
    return rebuilt, changed or (rebuilt != article_text)


class Command(BaseCommand):
    help = "Convert DebateArticle.article content into markdown-friendly format without rewording."

    def add_arguments(self, parser):
        parser.add_argument("--offset", type=int, default=0, help="Row offset in the ordered queryset")
        parser.add_argument("--limit", type=int, default=0, help="Rows to process (0 means all)")
        parser.add_argument("--apply", action="store_true", help="Persist changes. Without this flag, runs as dry-run.")

    def handle(self, *args, **options):
        offset = max(0, options["offset"])
        limit = max(0, options["limit"])
        apply_changes = options["apply"]

        qs = DebateArticle.objects.exclude(article__isnull=True).exclude(article__exact="").order_by("id")
        if offset:
            qs = qs[offset:]
        if limit:
            qs = qs[:limit]

        rows = list(qs)

        changed = 0
        heading_added = 0
        whitespace_only = 0
        changed_ids = []

        def build_new_text(row: DebateArticle) -> Tuple[str, bool, bool]:
            old_text = row.article or ""
            normalized = _normalize_whitespace(old_text)
            with_heading, did_add_heading = _ensure_top_heading(normalized, row.subTopic)
            with_structure, _ = _decorate_structure(with_heading)
            final_text, _ = _decorate_inline_labels(with_structure)
            did_change = final_text != old_text
            return final_text, did_change, did_add_heading

        if apply_changes:
            with transaction.atomic():
                for row in rows:
                    new_text, did_change, did_add_heading = build_new_text(row)
                    if not did_change:
                        continue

                    row.article = new_text
                    row.save(update_fields=["article", "updated_at"])
                    changed += 1
                    changed_ids.append(row.id)
                    if did_add_heading:
                        heading_added += 1
                    else:
                        whitespace_only += 1
        else:
            for row in rows:
                _, did_change, did_add_heading = build_new_text(row)
                if not did_change:
                    continue
                changed += 1
                changed_ids.append(row.id)
                if did_add_heading:
                    heading_added += 1
                else:
                    whitespace_only += 1

        mode = "APPLY" if apply_changes else "DRY-RUN"
        self.stdout.write(f"mode={mode}")
        self.stdout.write(f"selected_rows={len(rows)}")
        self.stdout.write(f"changed_rows={changed}")
        self.stdout.write(f"heading_added_rows={heading_added}")
        self.stdout.write(f"whitespace_only_rows={whitespace_only}")
        self.stdout.write(f"unchanged_rows={len(rows) - changed}")
        self.stdout.write(f"changed_ids={changed_ids}")
