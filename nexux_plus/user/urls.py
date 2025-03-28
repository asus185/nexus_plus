from django.urls import path
from .views import login_view, register_view, logout_view, register_view,products_add

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('products_add',products_add, name='products_add')
]
