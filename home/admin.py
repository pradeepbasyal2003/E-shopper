from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(ProductReview)
admin.site.register(Wishlist)
admin.site.register(Order)

