from django import forms

class Login(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id' : 'username','placeholder' : 'Enter Username'}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id' : 'password','placeholder' : 'Enter Password'}))

class Register(forms.Form):
    firstname = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id' : 'firstname','placeholder' : 'Enter Firstname'}))
    lastname = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id' : 'lastname','placeholder' : 'Enter Lastname'}))
    email = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'id' : 'email','placeholder' : 'Enter Email'}))
    password = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id' : 'password','placeholder' : 'Enter Password'}))
    repassword = forms.CharField(max_length=200,widget=forms.PasswordInput(attrs={'id' : 'repassword','placeholder' : 'Confirm Password'}),label="Confirm Password")
    hidden = forms.CharField(widget = forms.HiddenInput(attrs={'id' : 'hidden'}))