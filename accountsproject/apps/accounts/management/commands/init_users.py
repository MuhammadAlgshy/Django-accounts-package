import email
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from os import environ

USERS = [
    {
        "email": environ["SUPER_USERNAME"],
        "password": environ["SUPER_PASSWORD"],
        "is_staff": True,
        "is_active": True,
        "is_superuser": True,
    },
]


User = get_user_model()


class Command(BaseCommand):
    """
    Initialize users
    """

    @transaction.atomic
    def _init_users(self):
        for user in USERS:
            if User.objects.filter(email=user["email"]).exists():
               self.stdout.write(self.style.WARNING("Users already initialized"))
               return
            password = user.pop("password")
            newuser = User.objects.create(**user)
            newuser.set_password(password)
            newuser.save()
            self.stdout.write(self.style.SUCCESS("%d users inserted" % len(USERS)))

    def handle(self, *args, **options):
        self._init_users()
