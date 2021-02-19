"""inventory URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import dashboard

# from users.views import UserViewSet, GroupViewSet
from store.views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'order_api', OrderViewSet)
# router.register(r'api_users', UserViewSet)
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('store/', include('store.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
