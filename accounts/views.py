from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
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
        return HttpResponse("Logged In")
        #return redirect('/')
      else:
        return HttpResponse("Something Wrong")
    else:
      return HttpResponse("Not A User")
  else:
    return render(request, "login.html")

