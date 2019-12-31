from .models import Post
from django.shortcuts import render


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def hotel(request):
    return render(request, 'hotel.html')