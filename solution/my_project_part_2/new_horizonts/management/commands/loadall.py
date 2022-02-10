import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create fixtures from json file," "createfixtures [filename] [app.model]"

    def handle(self, *args, **options):
        # cars fixtures:
        os.system("python manage.py loaddata fixtures/reforms.json")
        os.system("python manage.py loaddata fixtures/alphabet.json")
        os.system("python manage.py loaddata fixtures/first_opened.json")
        os.system("python manage.py loaddata fixtures/pages.json")
        os.system("python manage.py loaddata fixtures/counting.json")
        os.system("python manage.py loaddata fixtures/users_geography.json")
