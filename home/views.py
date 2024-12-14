from django.shortcuts import render , redirect
from django.views import View
from .models import *
import random
from django.contrib import messages
from django.contrib.auth.models import User
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
            else:#just redirect('/') doesn't work we need to return it too.
                return redirect('/')
        self.views['brand_products'] = Product.objects.all()
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()

        return render(request, "search.html", self.views)

def signup(request):

    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        if password == c_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,"username not available")
                return redirect("/signup")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "email not available")
                return redirect("/signup")

            else:
                data = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                )
                data.save()
                messages.success(request,"account created..")
                return redirect("/account/login")
        else:
            messages.error(request,"the passwords donot match")
            return redirect("/signup")

    return render(request,"signup.html")


class CartView(Base):
    def get(self,request):
        username = request.user.username
        self.views['my_carts'] = Cart.objects.filter(username = username)
        grand_total = 0
        for items in self.views['my_carts']:
            grand_total += items.total
        self.views['grand_total'] = grand_total
        return render(request,'cart.html',self.views)

def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(username = username,slug = slug,checkout = False):
        product = Product.objects.get(slug = slug)
        price = product.price
        discounted_price = product.discounted_price
        quantity= Cart.objects.get(username = username,slug = slug,checkout = False).quantity +1
        if discounted_price > 0 :
            total = discounted_price * quantity
        else:
            total = price * quantity
        Cart.objects.filter(username=username, slug=slug, checkout=False).update(
            quantity = quantity,
            total = total,
        )
        return redirect('/cart')
    else:
        product = Product.objects.get(slug=slug)
        price = product.price
        discounted_price = product.discounted_price
        quantity = 1
        if discounted_price > 0:
            total = discounted_price
        else:
            total = price
        data = Cart.objects.create(
            username = username,
            slug = slug,
            quantity = quantity,
            total = total,
            items = Product.objects.filter(slug=slug)[0],
        )
        data.save()
    return redirect('/cart')

def subtract_item(request,slug):
    username = request.user.username
    if Cart.objects.filter(username = username,slug =slug, checkout=False):
        product = Product.objects.get(slug=slug)
        price = product.price
        discounted_price = product.discounted_price
        quantity = Cart.objects.get(username=username, slug=slug, checkout=False).quantity
        if quantity == 1:
            delete_item(request, slug)
        else:

            quantity = Cart.objects.get(username=username, slug=slug, checkout=False).quantity - 1
            if discounted_price > 0:
                total = discounted_price * quantity
            else:
                total = price * quantity
            Cart.objects.filter(username=username, slug=slug, checkout=False).update(
                quantity=quantity,
                total=total,
            )

    return redirect("/cart")

def delete_item(request,slug):
    username = request.user.username
    if Cart.objects.filter(username=username, slug=slug, checkout=False):
        Cart.objects.filter(username=username, slug=slug, checkout=False).delete()
    return redirect('/cart')