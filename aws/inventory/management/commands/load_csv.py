from csv import DictReader
from datetime import datetime
from django.core.management import BaseCommand
from inventory.models import Invs
from pytz import UTC

# ALREADY_LOADED_ERROR_MESSAGE = """
# If you need to reload the pet data from the CSV file,
# first delete the db.sqlite3 file to destroy the database.
# Then, run `python manage.py migrate` for a new empty
# database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from instances.csv into our Invs Model"

    def handle(self, *args, **options):
        if Invs.objects.exists():
            print('Inventory List already loaded...exiting.')
            return

        print("Creating Inventory data")

        print("Loading Inventory data for Inventory available for AWS")
        for row in DictReader(open('./inventory.csv')):
            inventoryitem = Invs()
            inventoryitem.instance_id = row['instance_id']
            inventoryitem.instance_type = row['instance_type']
            inventoryitem.ami_id = row['ami_id']
            inventoryitem.instance_status = row['instance_status']
            inventoryitem.availability_zone = row['availability_zone']
            inventoryitem.public_ip = row['public_ip']
            inventoryitem.private_ip = row['private_ip']
            inventoryitem.instance_keypair = row['instance_keypair']
            inventoryitem.dns_public = row['dns_public']
            inventoryitem.dns_private = row['dns_private']
            inventoryitem.save()
