from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from .serializers import UserSerializer
from rest_framework import generics
from .models import User
import json


def signup(request):
  if (request.method == "POST"):
    data = json.loads(request.body)
    user = User.objects.create_user(
      email = data["email"],
      name = data["name"],
      nickname = data["nickname"],
      birth = data["birth"],
      phonenumber = data["phonenumber"],
      password = data["password"]
    )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    auth.login(request, user)
    #return redirect('/')
    return HttpResponse("OK")
  return render(request, "signup.html")
