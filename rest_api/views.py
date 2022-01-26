from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, JsonResponse

class IndexView(View):
  def get(self, request):
    dummy = {
      'User_number': "11",
      'User_id': "admin",
      "User_password": "admin",
      "User_name": "아레브관리자",
      "User_phonenumber": "01012345678",
      "User_birth": "220126",
      "User_joindate": "220126",
      "User_rate": "0.00"
    }
    return JsonResponse(dummy)
  
  def post(self, request):
    return HttpResponse("POST")
  
  def put(self, request):
    return HttpResponse("PUT")
  
  def delete(self, request):
    return HttpResponse("Delete")

