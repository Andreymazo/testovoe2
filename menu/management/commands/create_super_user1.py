from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            username='andrey_mazo',
            is_superuser=True,
            is_staff=True
        )
        user.set_password('qwert123asd')
        user.save()
