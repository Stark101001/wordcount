from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name = "homepage"),
    path('count/', views.count, name="count"),
    path('about_page/',views.about_page, name = "about_page")
    
]

