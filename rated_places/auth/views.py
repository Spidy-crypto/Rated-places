from django.shortcuts import render
import sweetify
from django.contrib.auth.models import User,auth

def login(request):
    return render(request,'login.html')

def registration(request):

    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['repassword']

        user = User.objects.create_user(username = email,first_name = fname,last_name=lname,email=email,password = pass1)
        user.save()
        return render(request,'login.html')
    else:
        return render(request,'registration.html')