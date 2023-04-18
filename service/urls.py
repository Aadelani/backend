from django.urls import path
from . import views

urlpatterns = [
    path('calculate-cost/', views.calculate_cost, name='calculate_cost'),
    path('send-single-sms/', views.send_single_sms, name='send_single_sms'),
    path('send-bulk-sms/', views.send_bulk_sms, name='send_bulk_sms'),
    path('history/', views.history, name='history'),
]