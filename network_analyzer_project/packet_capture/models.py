# packet_capture/models.py
from django.db import models

class Packet(models.Model):
    source_ip = models.GenericIPAddressField()
    destination_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
