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
    path('add_review/<slug:slug>', add_review, name="add_review"),
    path('logout/',  CustomLogoutView.as_view(), name='logout'),
    path('wishlist/', WishlistView.as_view(), name="cart"),
    path('delete_from_wishlist/<slug>', delete_from_wishlist , name = "delete_from_wishlist"),
    path('add_to_wishlist/<slug>' , add_to_wishlist ,name="add_to_wishlist"),
    path('checkout',CheckoutView.as_view() ,name="checkout"),

]