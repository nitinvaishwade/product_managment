# from django.urls import path

# from .views import login_page, logout_page, register_page

# from rest_framework import routers
from django.urls import include, path
from .views import *

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)




urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register'),
]