from django.urls import path,include
from .import views
from user.views import login,register_view,products_add
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.main, name='main'),
    path('login', login, name='login'),
    path('register', register_view, name='register'),
    path('products_add', products_add, name='products_add')
]
