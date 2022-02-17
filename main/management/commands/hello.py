from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "mówi hello"

    def handle(self, *args, **options):
        self.stdout.write("Hello World!")
