from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-post'),
    path('about', views.about, name='blog-about'),
    path('hotel', views.hotel, name='blog-hotel'),

]