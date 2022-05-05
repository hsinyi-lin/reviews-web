import requests
from django.shortcuts import render

from core.settings import API_URL as root
root += 'book_review'


def index(request):
    return render(request, 'index.html')


def detail(request, pk):
    return render(request, 'detail.html')


def search(request):
    return render(request, 'critic_reviews.html')

