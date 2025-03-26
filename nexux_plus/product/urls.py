from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path('list/',product_list, name='product_list'),
    path('detail/<int:pk>/',product_detail, name='product_detail')
]
