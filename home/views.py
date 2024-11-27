from django.shortcuts import render
from django.views import View
from .models import *
import random
# Create your views here.

class Base(View):
    views = {}


class HomeView(Base):

    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Ad.objects.all()
        self.views['products'] = Product.objects.all()

        # here we store the products as list because we cant assign the whole object to an variable view garna lai yesto garna praxa
        self.product = list(Product.objects.filter(labels = "new"))
        random.shuffle(self.product)
        self.views['recommended_1'] = self.product
        random.shuffle(self.product)
        self.views['recommended_2'] = self.product
        #two recommended are used because we have two sliding section that has recomended and duitai same aauxa eeuta matra recommended vayo vane
        return render(request,'index.html',self.views)

class CategoryView(Base):
#slug use vako xa tesaile slug ni pass gareko
#slug is used for unique link only it has no use in database
#database ma category ko id products table ma stored hunxa cause of foreign key which can be seen below
    def get(self,request,slug):

        cat_id = Category.objects.get(slug = slug).id # slug = slug le index.html ma category for loop bata chaleko xa tellai execute garxa
        self.views['cat_products'] = Product.objects.filter(category_id = cat_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()


        return render(request,"category.html",self.views)

class BrandView(Base):
#slug use vako xa tesaile slug ni pass gareko
#slug is used for unique link only it has no use in database
#database ma category ko id products table ma stored hunxa cause of foreign key which can be seen below
    def get(self,request,slug):
        brand_id = Brand.objects.get(slug = slug).id # slug = slug le index.html ma category for loop bata chaleko xa tellai execute garxa
        self.views['brand_products'] = Product.objects.filter(brand_id = brand_id)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()


        return render(request,"brands.html",self.views)



class ProductDetails(Base):

    def get(self,request,slug):
        self.views['product_details'] = Product.objects.filter(slug = slug)
        return render(request,"product-details.html",self.views)
