from django.urls import path
from .views import get_items

urlpatterns = [
    path('items/', get_items),
]