from django.urls import path
from .views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    ContentListCreateAPIView,
    ContentRetrieveUpdateDestroyAPIView,
    ContentSearchAPIView
)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('contents/', ContentListCreateAPIView.as_view(), name='content-list-create'),
    path('contents/<int:pk>/', ContentRetrieveUpdateDestroyAPIView.as_view(), name='content-retrieve-update-destroy'),
    path('contents/search/', ContentSearchAPIView.as_view(), name='content-search'),
]
