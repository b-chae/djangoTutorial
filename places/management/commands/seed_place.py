from django.core.management.base import BaseCommand
from users.models import User
from places.models import Place
import random


class Command(BaseCommand):
    help = "seed random places"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many places do you want me to create?",
        )

    def handle(self, *args, **options):
        number = options.get('number')

        for i in range(number):
            user = User.objects.all()[0]
            new_place = Place(
                name="Random Place",
                address="Random Address",
                phone_number="010-0000-0000",
                type="Random type",
                description="Random description",
                owner=user
            )
            new_place.save()

        print("SUCCESS: Places created!")
