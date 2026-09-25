from django.core.management.base import BaseCommand
from vaishnava_calendar.services.generator import generate_calendar_for_year


class Command(BaseCommand):
    help = 'Dynamically generate Vaishnava calendar days, observances, and stories for a given year using GCal engine.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--year',
            type=int,
            required=True,
            help='Year to calculate (e.g. 2026, 2027, 2028)'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force recalculation even if the year already exists in the database'
        )

    def handle(self, *args, **options):
        year = options['year']
        force = options.get('force', False)

        self.stdout.write(self.style.NOTICE(f"Generating Vaishnava calendar for year {year} (force={force})..."))
        result = generate_calendar_for_year(year=year, force=force)

        if result.get('status') == 'already_exists':
            self.stdout.write(
                self.style.WARNING(
                    f"Calendar for {year} already exists with {result.get('days_count')} days. Use --force to regenerate."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully generated {result.get('days_count')} days and "
                    f"{result.get('observances_count')} observances for year {year}."
                )
            )
            story_sum = result.get('story_summary', {})
            self.stdout.write(f"Attached stories summary: {story_sum}")
