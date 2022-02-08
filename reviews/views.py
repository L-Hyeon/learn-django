from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Review
import json

def writeReview(request):
  if (request.method == "POST"):
    data = json.loads(request.body)
    review = Review.objects.create_review(
      score = data["score"],
      content = data["content"],
      cntImg = data["cntImg"],
      images = data["images"],
      numItem = data["numItem"],
      numWriter = data["numWriter"]
    )

    # 아이템 상세 정보 창으로 리다이렉트
    #return redirect('items')
    return HttpResponse("OK")
  return render(request, "writeReview.html")

