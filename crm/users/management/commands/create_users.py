# from django.contrib.auth.models import User/
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
# from users.models import User
from crm.users.models import User
from faker import Faker




class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
        parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']
        fake = Faker()

        # for _ in range(10):
        # print(fake.name())
        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string(10))
            else:
                username = get_random_string(10)

            if admin:
                User.objects.create_superuser(username=username,name=fake.name(), email=fake.free_email(), password='admin@123')
            else:
                User.objects.create_user(username=username,name=fake.name(), email=fake.free_email(), password='admin@123')