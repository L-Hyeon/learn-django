from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
import json

def apply(request):
  if (request.method == "POST"):
    data = json.loads(request.body.decode('utf-8'))
    
    item = Item.objects.create_item(
      title = data["title"],
      category = data["category"],
      content = data["content"],
      location = data["location"],
      imageCnt = data["imageCnt"],
      images = data["images"]
    )
    #return redirect('/')
    return HttpResponse("OK")
  return render(request, "apply.html")

