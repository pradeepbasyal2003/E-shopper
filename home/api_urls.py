from .api_views import *
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]