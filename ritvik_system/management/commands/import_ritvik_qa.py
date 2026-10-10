import json
from django.core.management.base import BaseCommand
from django.db import transaction
from ritvik_system.models import (
    RitvikSection,
    RitvikSectionTranslation,
    RitvikQA,
    RitvikQATranslation,
)


class Command(BaseCommand):
    help = 'Import Ritvik system sections and questions from JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            required=True,
            help='Path to the ritvik_data.json file',
        )
        parser.add_argument(
            '--lang',
            type=str,
            default='en',
            help='Language code (default: en)',
        )

    def handle(self, *args, **options):
        file_path = options['file']
        lang = options['lang']

        self.stdout.write(f"Reading data from {file_path} for language '{lang}'...")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        sections_data = data.get('sections', [])
        questions_data = data.get('questions', [])

        with transaction.atomic():
            self.stdout.write("Importing sections...")
            section_map = {}
            for s in sections_data:
                sec_obj, _ = RitvikSection.objects.update_or_create(
                    section_number=s['section_number'],
                    defaults={
                        'slug': s.get('slug', f"section-{s['section_number']}"),
                        'order': s.get('order', s['section_number']),
                    }
                )
                RitvikSectionTranslation.objects.update_or_create(
                    section=sec_obj,
                    language=lang,
                    defaults={
                        'title': s['title'],
                        'description': s.get('description', ''),
                    }
                )
                section_map[s['section_number']] = sec_obj
                self.stdout.write(f"  [OK] Section {s['section_number']}: {s['title']}")

            self.stdout.write(f"\nImporting {len(questions_data)} questions...")
            imported_count = 0
            for q in questions_data:
                sec_obj = section_map.get(q['section_number'])
                if not sec_obj:
                    self.stderr.write(f"  [SKIP] Section {q['section_number']} not found for {q['question_code']}")
                    continue

                qa_obj, _ = RitvikQA.objects.update_or_create(
                    slug=q['slug'],
                    defaults={
                        'section': sec_obj,
                        'question_code': q['question_code'],
                        'order': q.get('order', 0),
                        'is_published': True,
                    }
                )

                RitvikQATranslation.objects.update_or_create(
                    qa_parent=qa_obj,
                    language=lang,
                    defaults={
                        'question': q['question'],
                        'answer': q['answer'],
                        'summary': q.get('summary', ''),
                    }
                )
                imported_count += 1

            self.stdout.write(
                self.style.SUCCESS(
                    f"\nSuccessfully imported {len(sections_data)} sections and {imported_count} questions (Language: {lang})!"
                )
            )
