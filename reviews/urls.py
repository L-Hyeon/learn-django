from django.urls import path

from . import views

urlpatterns = [
    path('writeReview/', views.writeReview, name='writeReview'),
]
