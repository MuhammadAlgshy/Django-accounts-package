from allauth.socialaccount.models import SocialApp
from django.core.management.base import BaseCommand
from django.db import transaction
from os import environ



SocialappList = [
    {
        "provider": "google",
        "name": "Google",
        "client_id": environ["GOOGLE_CLIENT_ID"],
        "secret": environ["GOOGLE_SECRET"],
    },
    {
        "provider": "microsoft",
        "name": "Microsoft",
        "client_id": environ["MS_CLIENT_ID"],
        "secret": environ["MS_SECRET"],
        
    },
]



class Command(BaseCommand):
    """
    Initialize Social Apps
    """

    @transaction.atomic
    def _init_providers(self):
        self.stdout.write(self.style.NOTICE("===== Initate Social Application ====="))
        rowsadded=0
        rowsskipped=0
        for socialapp in SocialappList:
            if SocialApp.objects.filter(name=socialapp.get('name')).exists():
               #self.stdout.write(self.style.WARNING(organization.get('code'))+" Org already exists!")
               rowsskipped+=1
            else:
                rowsadded+=1
                newsocialapp = SocialApp.objects.create(**socialapp)
                newsocialapp.save()
        self.stdout.write(self.style.SUCCESS(str(rowsadded))+" rows inserted! and " + self.style.SUCCESS(str(rowsskipped))+" rows already inserted! ")

    def handle(self, *args, **options):
        self._init_providers()
