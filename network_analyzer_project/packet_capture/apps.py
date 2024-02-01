from django.apps import AppConfig


class PacketCaptureConfig(AppConfig):
    name = 'packet_capture'
INSTALLED_APPS = [
    # other apps...
    'packet_capture',
]
