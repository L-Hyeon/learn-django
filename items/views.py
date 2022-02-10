from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
import json

def apply(request):
  if (request.method == "POST"):
    data = json.loads(request.body.decode('utf-8'))
    loc = data["location"] + ' ' + data["detailLoc"]
    item = Item.objects.create_item(
      title = data["title"],
      category = data["category"],
      content = data["content"],
      postcode = data["postcode"],
      location = loc,
      cntImg = data["cntImg"],
      images = data["images"],
      price = data["price"],
      pricePerHour = data["pricePerHour"],
    )
    #return redirect('/')
    return HttpResponse("OK")
  return render(request, "apply.html")

