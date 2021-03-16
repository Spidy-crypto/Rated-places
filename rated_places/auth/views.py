from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .forms import *
import sweetify

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            sweetify.error(request,"Username or password incorrect",button = "Ok",persistent = True)
    form = Login()
    return render(request,"login.html",{'form' : form})

def registration(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']

        if pass1 == pass2:
            if User.objects.filter(username=email).exists():
                sweetify.error(request,"User Already exist", button = 'Ok',persistent = True)
            else:
                user = User.objects.create_user(username = email,first_name = fname,last_name=lname,email=email,password = pass1)
                user.save()
                return redirect('/auth/login')
        else:
            sweetify.error(request, 'Passwords are not same', button='Ok',persistent = True)
    return render(request,"registration.html",{'form' : Register()})

def logout(request):
    auth.logout(request)
    return redirect("/")