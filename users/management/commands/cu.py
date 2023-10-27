""" Create user """

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@example.com',
            first_name='Lorem',
            last_name='Ipsum',
        )
        user.set_password('my_paSs3')
        user.save()
