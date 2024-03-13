from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemListCreateAPIView,SingleMenuItemView,msg
from rest_framework import routers

urlpatterns = [
    path('menu-items/', MenuItemListCreateAPIView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
    
]