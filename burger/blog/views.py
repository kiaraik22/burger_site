from django.shortcuts import render
from .models import Post

# Create your views here.

def create_post(request):
    return render(request, 'blog/main.html')