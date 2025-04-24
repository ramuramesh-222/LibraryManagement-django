from django.shortcuts import render,redirect #reload automatically is redirect
from .forms import *   
from .models import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

'''
def productsadd(request):

    context = {
        'product_form' : Product_Form()
    }


    if request.method == "POST":
        product_form = Product_Form(request.POST)

        if product_form.is_valid():
            product_form.save()

    return render(request,'products_add.html',context )

    def allproducts(request):
    context = {
        "all_products" : Product.objects.all()
    }
    all_products = Product.objects.all()
    return render(request,'products.html', context)

def deleteproduct(request,id):

    selected_product = Product.objects.get(id = id)

    selected_product.delete()

    return redirect('/inventory/products/')

def updateproduct(request,id):

    selected_product = Product.objects.get(id = id)

    context = {

        "product_form" : Product_Form(instance=selected_product)

    }

    if request.method == 'POST' :
        product_form = Product_Form(request.POST,instance=selected_product)

        if product_form.is_valid():
            product_form.save()

        return redirect('/inventory/products/')
        
    return render(request,'products_add.html',context)
'''

class productaddview(LoginRequiredMixin,View):
    login_url='/'  
    def get(self,request):
        print("LSKJ")

        context = {
            'product_form' : Product_Form()
        }

        return render(request,'products_add.html',context )
    
    
    login_url='/'  
    def post(self,request):
        print("NGIK")

        product_form = Product_Form(request.POST, request.FILES)

        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')


class listprodectview(LoginRequiredMixin,View):

    login_url='/'  
    def get (self,request):
        context = {
        "all_products" : Product.objects.all()
        }
        all_products = Product.objects.all()
        return render(request,'products.html', context)
    

class prodectdeleteview(LoginRequiredMixin,View):
    login_url='/'  
    def get (self,request,id):

        selected_product = Product.objects.get(id = id)

        selected_product.delete()

        return redirect('/inventory/products/')
    
class productdeleteview(LoginRequiredMixin,View):

    login_url='/'  
    def get (self,request,id):
        selected_product = Product.objects.get(id = id)

        context = {

            "product_form" : Product_Form(instance=selected_product)

        }
        return render(request,'products_add.html',context)

 
    def post (self,request,id):
        selected_product = Product.objects.get(id = id)

        product_form = Product_Form(request.POST,instance=selected_product)

        if product_form.is_valid():
            product_form.save()
        return redirect('/inventory/products/')
        
            