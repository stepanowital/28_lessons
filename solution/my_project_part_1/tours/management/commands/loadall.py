import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create fixtures from json file," "createfixtures [filename] [app.model]"

    def handle(self, *args, **options):
        # cars fixtures:
        os.system("python manage.py loaddata fixtures/tours.json")
        os.system("python manage.py loaddata fixtures/spb_points.json")
        os.system("python manage.py loaddata fixtures/feedback_cities.json")
        os.system("python manage.py loaddata fixtures/feedback_tours.json")
        os.system("python manage.py loaddata fixtures/feedbackupdate_cities.json")
        os.system("python manage.py loaddata fixtures/feedbackupdate_tours.json")
        os.system("python manage.py loaddata fixtures/feedbackupdate_review.json")
        os.system("python manage.py loaddata fixtures/feedbackdelete_cities.json")
        os.system("python manage.py loaddata fixtures/feedbackdelete_tours.json")
        os.system("python manage.py loaddata fixtures/feedbackdelete_review.json")
