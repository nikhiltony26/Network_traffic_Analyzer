# packet_capture/views.py
from django.shortcuts import render
from scapy.all import sniff, Ether, IP
from .models import Packet

def capture_packets():
    sniff(prn=packet_callback)

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        Packet.objects.create(source_ip=ip_src, destination_ip=ip_dst)

def index(request):
    return render(request, 'index.html')

def start_capture(request):
    capture_packets()
    return render(request, 'capture_started.html')

def stop_capture(request):
    # Stop the capture (implement as needed)
    return render(request, 'capture_stopped.html')

def show_results(request):
    packets = Packet.objects.all()
    return render(request, 'results.html', {'packets': packets})
