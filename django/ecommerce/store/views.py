from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.http.response import JsonResponse
from django.contrib.auth import authenticate, login, logout
from.forms import CustomerRegistrationForm, LoginForm
from django.views import View
# Create your views here.
def home(request):
   trending_products = Product.objects.filter(trending=1)
   context = {'trending_products':trending_products}
   return render(request, "store/index.html",context)

def Collections(request):
   category = Category.objects.filter(status=0)
   context = {'category':category}
   return render(request,"store/Collections.html",context)

def collectionsview(request,slug):
   if(Category.objects.filter(slug=slug,status=0)):
      products = Product.objects.filter(category__slug=slug)
      category = Category.objects.filter(slug=slug).first()
      context = {'products': products,'category':category}
      return render(request,"store/products/index.html",context)
   else:
      messages.warning(request,"No such category found")
      return redirect('Collections')
    
def productview(request, cate_slug, prod_slug):
   if(Category.objects.filter(slug=cate_slug,status=0)):
      if(Product.objects.filter(slug=prod_slug,status=0)):
         products = Product.objects.filter(slug=prod_slug,status=0).first
         context = {'products':products}
      else:
         messages.error(request,"No such product found")
         return redirect('Collections')

   else:
      messages.error(request,"No such category found")
      return redirect('Collections')   
   return render(request,"store/products/view.html",context)

def productlistAjax(request):
   products = Product.objects.filter(status=0).values_list('name',flat=True)
   productsList = list(products)

   return JsonResponse(productsList, safe=False )

def searchproduct(request):
   if request.method == 'POST':
      searchedterm = request.POST.get('productsearch')
      if searchedterm == "":
         return redirect(request.META.get('HTTP_REFERER'))
      else:
         product = Product.objects.filter(name__contains=searchedterm).first()
         if product:
            return redirect('Collections/'+product.category.slug+'/'+product.slug)
         else:
            messages.info(request,"No product matched your search")
            return redirect(request.META.get('HTTP_REFERER'))
   return redirect(request.META.get('HTTP_REFERER'))


def register(request):
   form = CustomerRegistrationForm()
   if request.method =='POST':
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,"Registered Successfully! Login to Continue")
         return redirect('/login')
   context = {'form':form} 
   return render(request,"store/auth/register.html",context)

def loginpage(request):
   form = LoginForm()
   if request.method =='POST':
      form = LoginForm(request.POST)
      if request.user.is_authenticated:
         messages.warning(request, "You are already logged in")
         return redirect('/')
      else:
         if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
               login(request,user)
               messages.success(request,"Logged in Successfully")
               return redirect("/")
            else:
               messages.error(request,"Invalid Username or Password")
               return redirect('/login')
   context = {'form':form} 
   return render(request,"store/auth/login.html",context)

def logoutpage(request):
   if request.user.is_authenticated:
         logout(request)
         messages.success(request,"Logged out Successfully")
   return redirect("/")




   
    