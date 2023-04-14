from django.core.management import BaseCommand

from menu.models import MenuItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        ii = [
            {"name": "Very Much Hard Rock", "url": "hard_rock", "parent_id": 1},
            {"name": "Pop Rock", "url": "pop_rock", "parent_id": 1},
            {"name": "Hard Rock", "url": "hard_rock", "parent_id": 1}
        ]

        for i in ii:
            rec_1 = MenuItem(name=i["name"], url=i["url"], parent_id=i["parent_id"])
            rec_1.save()

