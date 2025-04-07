from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.event_create, name='event_create'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
]
