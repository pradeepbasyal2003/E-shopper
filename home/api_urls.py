from .api_views import *
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product_filter' ,ProductListView.as_view() , name="product_filter"),
    path('product_crud/<int:pk>', ProductDetail.as_view(), name="product_crud"),
    path('product_add', ProductList.as_view(), name="product_add"),

]