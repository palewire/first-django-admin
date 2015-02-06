import os
import csv
from django.conf import settings
from academy.models import Invite
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        print "Loading CSV"
        csv_path = os.path.join(settings.BASE_DIR, "academy_invites_2014.csv")
        csv_file = open(csv_path, 'rb')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj = Invite.objects.create(name=row['Name'], branch=row['Branch'])
            print obj