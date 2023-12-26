from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from decouple import config

from rest_framework.authtoken.models import Token


DJANGO_SUPERUSER_PASSWORD = config('DJANGO_SUPERUSER_PASSWORD', cast=str)
DJANGO_SUPERUSER_USERNAME = config('DJANGO_SUPERUSER_USERNAME', cast=str)
DJANGO_SUPERUSER_EMAIL = config('DJANGO_SUPERUSER_EMAIL', cast=str)
DJANGO_SUPERUSER_AUTH_TOKEN = config('DJANGO_SUPERUSER_AUTH_TOKEN', cast=str)


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        try:
            instance = User.objects.filter(username=DJANGO_SUPERUSER_USERNAME).first()
            if instance:
                return self.stdout.write(self.style.SUCCESS('Successfully get existing superuser'))

            user = User.objects.create_superuser(
                username=DJANGO_SUPERUSER_USERNAME,
                email=DJANGO_SUPERUSER_EMAIL,
                password=DJANGO_SUPERUSER_PASSWORD
            )

            user.is_superuser = True
            user.is_staff = True
            user.is_admin = True

            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))

            token, created = Token.objects.get_or_create(
                user=user,
                key=DJANGO_SUPERUSER_AUTH_TOKEN
            )

            self.stdout.write(self.style.SUCCESS(f'Token {"successfully created" if created else "successfully exists"}'))

        except Exception as e:
            raise CommandError(e)

