from django.urls import path
from . import views

urlpatterns = [
    path('omah/', views.home ),
    path('berita/', views.berita),
    path('temp/', views.temp ),
    path('about/', views.about),
]