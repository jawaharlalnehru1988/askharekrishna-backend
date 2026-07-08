from django.db import migrations


# Map of DB ID → correct hyphenated sloka_number string
# All 22 confirmed bad records
CORRECTIONS = {
    19:  '17-18',
    22:  '21-22',
    34:  '37-38',
    32:  '32-33-34-35',
    84:  '42-43',
    224: '27-28',
    236: '11-12',
    237: '13-14',
    243: '20-21-22-23',
    368: '12-13',
    407: '10-11',
    422: '26-27',
    436: '41-42',
    459: '13-14',
    463: '18-19',
    471: '8-9-10',
    515: '22-23-24-25',
    536: '1-2-3',
    544: '11-12',
    545: '13-14-15',
    579: '26-27',
    631: '51-52-53',
}


def fix_sloka_numbers_and_populate_start(apps, schema_editor):
    Video = apps.get_model('videos', 'Video')

    # Step 1: Fix the 22 bad concatenated records
    for pk, correct_value in CORRECTIONS.items():
        try:
            video = Video.objects.get(pk=pk)
            video.sloka_number = correct_value
            # Compute sloka_start from the corrected value
            try:
                video.sloka_start = int(correct_value.split('-')[0])
            except (ValueError, IndexError):
                video.sloka_start = 0
            video.save()
        except Video.DoesNotExist:
            pass  # Record may have been deleted; safe to skip

    # Step 2: Populate sloka_start for ALL remaining records that still have 0
    # (i.e., valid single-number slokas that were never corrected above)
    for video in Video.objects.filter(sloka_start=0):
        try:
            video.sloka_start = int(str(video.sloka_number).split('-')[0])
        except (ValueError, IndexError):
            video.sloka_start = 0
        video.save()


def reverse_fix(apps, schema_editor):
    # Reversal: reset sloka_start to 0 for corrected records
    Video = apps.get_model('videos', 'Video')
    for pk in CORRECTIONS.keys():
        try:
            video = Video.objects.get(pk=pk)
            video.sloka_start = 0
            video.save()
        except Video.DoesNotExist:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_sloka_number_to_charfield_add_sloka_start'),
    ]

    operations = [
        migrations.RunPython(
            fix_sloka_numbers_and_populate_start,
            reverse_code=reverse_fix,
        ),
    ]
