from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate

from learn_django.settings import ALGORITHM, SECRET_KEY
from .models import User
import json

def signup(request):
  if (request.method == "POST"):
    data = json.loads(request.body.decode('utf-8'))
    
    user = User.objects.create_user(
      email = data["email"],
      name = data["name"],
      nickname = data["nickname"],
      birth = data["birth"],
      phonenumber = data["phone"],
      password = data["password"]
    )
    auth.login(request, user)
    #return redirect('/')
    return HttpResponse("OK")
  return render(request, "signup.html")

def login(request):
  if (request.method == "POST"):
    data = json.loads(request.body.decode('utf-8'))
    if (User.objects.filter(email=data["email"]).exists()):
      user = auth.authenticate(request, username=data["email"], password=data["password"])
      if (user is not None):
        auth.login(request, user)
        SECRET = SECRET_KEY
        token = jwt.encode({'usernumber': user.usernumber}, SECRET, algorithm = ALGORITHM)
        return HttpResponse("Logged In")
        #return redirect('/')
      else:
        return HttpResponse("Wrong Password")
    else:
      return HttpResponse("Not A User")

  else:
    return render(request, "login.html")

def logout(request):
  response = render(request, '/')
  auth.logout(request)
  return response

def change_pw(request):
  if (request.method != "POST"):
    return HttpResponse("Access Denied")
  data = json.loads(request.body)
  newPassword = data["newPassword"]
  user = request.user
  user.set_password(newPassword)
  user.save()
  auth.login(user)
  return HttpResponse("Password Changed")
  #return redirect('/')

def tokenChk(request):
  if (request.method != "POST"):
    return HttpResponse("Access Denied")
  
