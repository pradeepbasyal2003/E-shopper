from django.shortcuts import render , redirect
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
        product_category = Product.objects.get(slug = slug).category_id
        self.views['related_products'] = Product.objects.filter(category_id = product_category)
        return render(request,"product-details.html",self.views)


class SearchView(Base):
#for searching we made the logic below and in the template we make a form tag with method get.
#then we need to make the action="nameofurl" in this case "search" kinaki we are searching from a different page that doesn't send the request to this page.
    def get(self, request):
        if request.method == "GET":
            query = request.GET['query']
            if query != "":
                self.views['search_products'] = Product.objects.filter(name__icontains = query) #__icontains is used to make it case insensitive
            else :
                redirect('/')
        self.views['brand_products'] = Product.objects.all()
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()

        return render(request, "search.html", self.views)

