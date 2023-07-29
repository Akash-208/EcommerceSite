from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Cart
from django import forms 

# -----------------------------------------HOME--------------------------------------------------

def index(request):
    AllProd = tuple(Product.objects.all())
    Cartproducts = Cart.objects.all() 
    CategAvailable = set()
    for product in AllProd:
        CategAvailable.add(product.category)
      
    parameters = {"AllProd":AllProd,"CategAvailable":sorted(CategAvailable),'NumInCart':len(Cartproducts)}
    return render(request,'shop-home2.html',parameters)

# ----------------------------------------ABOUT--------------------------------------------------

def about(request):
    Cartproducts = Cart.objects.all() 
    params = {'NumInCart':len(Cartproducts)}
    return render(request,'about.html',params)

# ------------------------------------ADD TO CART------------------------------------------------

def cartdb(request,id):
    
    ana = request.POST.get('number')
    if ana == None:
        ana = 1
    else:
        ana = ana
    props = Product.objects.get(product_id = id)
    name = props.product_name
    description = props.desc
    price = props.price
    image = props.image
    Cart(Cprod_id = id, Cprod_name = name, Cdesc = description, Cprice = price, Cimage = image, Cquantity = ana).save()
    return redirect("home")

# ------------------------------------PRODUCT VIEW-----------------------------------------------

def prodView(request,id):
    Cartproducts = Cart.objects.all() 
    props = Product.objects.get(product_id = id)
    name = props.product_name
    description = props.desc
    price = props.price
    prodImage = props.image
    params = {'title':name,'price':price,'desc':description,'pimage':prodImage,'ID':id,'NumInCart':len(Cartproducts)}
    return render(request,'productview.html',params)

# ---------------------------------------CART----------------------------------------------------

def viewCart(request):

    allcartprod = Cart.objects.all()
    sum = 0
    for prod in allcartprod:
        sum = sum + (prod.Cprice*prod.Cquantity)
    return render(request,'cart.html',{'ap':allcartprod,'prodInCart':len(allcartprod),'total':sum})

# ----------------------------------Removing cart items----------------------------------------
def remove(request,id):
    x = Cart.objects.get(Cprod_id = id)
    x.delete()
    return redirect('viewcart')



def analyze(request):
    ana = request.POST.get('number')
    return HttpResponse(ana)

# -----------------------------------------------------------------------------------------------
    
# def contact(request):
#     return HttpResponse('This is contact page')

# def tracker(request):
#     return HttpResponse("We are at tracker")


# def checkout(request):
#     return HttpResponse("We are at the checkout page")

# def search(request):
#     return HttpResponse('This is the search page')



