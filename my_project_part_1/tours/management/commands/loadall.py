import os

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads fixtures from fixtures dir"
    fixtures_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filenames = [
        "tours.json",
        "spb_points.json",
        "feedback_cities.json",
        "feedback_tours.json",
        "feedbackupdate_cities",
        "feedbackupdate_tours",
        "feedbackupdate_review",
        "feedbackdelete_cities",
        "feedbackdelete_tours",
        "feedbackdelete_review",
    ]

    def handle(self, *args, **options):
        for fixture_filename in self.filenames:
            call_command(self.loaddata_command, os.path.join(self.fixtures_dir, fixture_filename))
