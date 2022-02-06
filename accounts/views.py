from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .models import User
import json


def signup(request):
  if (request.method == "POST"):
    data = json.loads(request.body)
    user = User.objects.create_user(
      email = request.POST.get("email"),
      name = request.POST.get("name"),
      nickname = request.POST.get("nickname"),
      birth = request.POST.get("birth"),
      phonenumber = request.POST.get("phonenumber"),
      password = request.POST.get("password")
    )
    auth.login(request, user)
    return redirect('/')
  return render(request, "signup.html")