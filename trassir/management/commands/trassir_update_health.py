from django.core.management.base import BaseCommand

from trassir.models import NVR, Health
import json
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):

        servers = NVR.objects.all()
        for server in servers:
            health = Health(server=NVR.objects.get(pk=server.id))
            health.health = json.dumps(NVR.objects.get(pk=server.id).get_health())
            health.collected_at = datetime.datetime.now()
            health.save()
