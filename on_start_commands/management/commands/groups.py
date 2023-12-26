from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand, CommandError

from decouple import config


DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)
DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)
DJANGO_SUPERUSER_AUTH_TOKEN = config('DJANGO_SUPERUSER_AUTH_TOKEN', cast=str)


class Command(BaseCommand):
    help = 'Create magic groups'

    def handle(self, *args, **options):
        try:
            mage_first_level_group, created = Group.objects.get_or_create(name='Mage First Level')
            self.stdout.write(self.style.SUCCESS(f'Mage First Level created status: {"created" if created  else "exist"}'))

            mage_second_level_group, created = Group.objects.get_or_create(name='Mage Second Level')
            self.stdout.write(self.style.SUCCESS(f'Mage Second Level status: {"created" if created  else "exist"}'))

            mage_third_level_group, created = Group.objects.get_or_create(name='Mage Third Level')
            self.stdout.write(self.style.SUCCESS(f'Mage Third Level: {"created" if created  else "exist"}'))

        except Exception as e:
            raise CommandError(e)

