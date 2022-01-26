from django.urls import path
from . import views

app_name = "rest_api"
urlpatterns = [
  path('', views.IndexView.as_view(), name="index")
]