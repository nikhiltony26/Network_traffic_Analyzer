# packet_capture/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start_capture/', views.start_capture, name='start_capture'),
    path('stop_capture/', views.stop_capture, name='stop_capture'),
    path('results/', views.show_results, name='show_results'),
]
