from django.urls import path
from .views import items,delete_item,update_item

urlpatterns = [
    path('items/', items),
    path('items/<int:id>/', delete_item),
    path('items/update/<int:id>/', update_item),

]