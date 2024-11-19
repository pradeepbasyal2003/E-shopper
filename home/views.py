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