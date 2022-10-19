from django.core.management.base import BaseCommand
from posts.utils import create_posts

class Command(BaseCommand):
    help = "dodaje fejkowe posty"

    def handle(self, *args, **options):
        # print ('no dobra dodjaę')
        count = options.get('count')
        create_posts(
            options.get('count')
        )
        self.stdout.write('posts has been created')
    #ta metoda odpowiada za wywołanie posta
    # self bo to programowanie obiektowe
    # tworzymy metodę nie funkcję więc *args
    # **kwargs bo będziemy przyjmować nazwane i nienazwane argumenty (tutaj **options)

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            type=int,
            default=10,
            dest='count',
            help='Amount of posts to generate'
        )
        # pass

    # argument, który będzie dopuszczalny ma być listą postów