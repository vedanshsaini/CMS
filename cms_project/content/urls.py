# urls.py in content app folder
from django.urls import path
from .views import content_list, content_detail

urlpatterns = [
    path('content/', content_list, name='content_list'),
    path('content/<int:pk>/', content_detail, name='content_detail'),
]
