from django.core.management import BaseCommand

from menu.models import Menu


class Command(BaseCommand):

    def handle(self, *args, **options):
        ii = [
            {"name": "Rock", "url": "rock"},
            {"name": "Blues", "url": "blues"},
            # {"name": "Menu_Item_Third", "url": "Third"}
        ]

        for i in ii:
            rec_1 = Menu(name=i["name"], url=i["url"])
            rec_1.save()
