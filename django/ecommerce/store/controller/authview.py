from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.contrib import messages
#from store.forms import CustomUserForm
# Create your views here.

#def register(request):
   # form = CustomUserForm()
    #if request.method =='POST':
     #   form = CustomUserForm(request.POST)
      #  if form.is_valid():
       #     form.save()
        #    messages.success(request,"Registered Successfully! Login to Continue")
         #   return redirect('/login')
    #context = {'form':form} 
    #return render(request,"store/auth/register.html",context)



def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")


