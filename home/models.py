from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=500 , unique = True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="media")
    description = models.TextField(blank = True)
    rank = models.IntegerField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='media' , blank=True)
    numbers_of_products = models.IntegerField(default = 1)
    slug = models.CharField(max_length=500 , blank = True)
    def __str__(self):
        return self.name

STOCK = (('in stock' , 'In Stock') , ('out of stock' , 'Out Of Stock'))
LABELS = (('','default'), ('new' , 'new'), ('hot' , 'hot') , ('sale' , 'sale'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    specification = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(choices = STOCK , max_length=50)
    labels = models.CharField(choices = LABELS , max_length=50 , blank=True)
    slug = models.CharField(max_length= 500 , blank = True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    username = models.CharField(max_length=500)
    slug = models.CharField(max_length=300)
    quantity = models.FloatField()
    total = models.FloatField()
    items = models.ForeignKey(Product, on_delete= models.CASCADE )
    date = models.DateTimeField(auto_now_add=True)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class ProductReview(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField()
    comment = models.TextField()
    def __str__(self):
        return self.username

class Wishlist(models.Model):
    username = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    items = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username