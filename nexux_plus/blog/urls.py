from django.urls import path
from .views import blog_view

urlpatterns = [
    path('',blog_views, name='blog'),
]