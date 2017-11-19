import os

from django.core.management.base import BaseCommand
	
from usermodel.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(email="prabhat@example.com").exists():
            User.objects.create_superuser("prabhat@example.com", "pass12345")