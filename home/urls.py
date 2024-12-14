from django.urls import path , include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name="category"),
    path('brand/<slug>', BrandView.as_view(), name="brand"),
    path('product/<slug>', ProductDetails.as_view() , name='product'),
    path('search', SearchView.as_view() , name="search"),
    path('signup', signup , name="signup"),
    path('cart/', CartView.as_view() , name="cart"),
    path('add_to_cart/<slug>', add_to_cart, name="add_to_cart"),
    path('delete_item/<slug>', delete_item, name="delete_item"),
    path('subtract_item/<slug>', subtract_item, name="subtract_item"),

]