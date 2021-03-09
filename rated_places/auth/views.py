from django.shortcuts import render,redirect
import sweetify
from django.contrib.auth.models import User,auth

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")

    return render(request,"login.html")

def registration(request):

    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        # pass2 = request.POST['repassword']

        user = User.objects.create_user(username = email,first_name = fname,last_name=lname,email=email,password = pass1)
        user.save()
        
        return redirect("/auth/login")
    else:
        return render(request,"registration.html")

def logout(request):
    auth.logout(request)
    return redirect("/")