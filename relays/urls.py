from django.urls import path
from . import views

urlpatterns = [
    path('relays/', views.relay_list, name='relay_list'),
]
