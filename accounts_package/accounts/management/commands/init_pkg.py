import subprocess
import sys
from django.core.management.base import BaseCommand

packages = ['django-allauth','dj_rest_auth','djangorestframework-simplejwt','djangorestframework']
    
class Command(BaseCommand):
    """
    Install packages django-allauth, dj-rest-auth, djangorestframework-simplejwt, djangorestframework
    """

    def _init_pkg(self):
        for package in packages:
            subprocess.check_call([sys.executable, "-m", "pipenv", "install", package])

    def handle(self, *args, **options):
        self._init_pkg()