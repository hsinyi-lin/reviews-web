import requests
from django.shortcuts import render

from core.settings import API_URL as root
root += 'book_review'


def index(request):
    r = requests.get(f'{root}/all/')
    # print(r.text)
    # print(r.json())
    result = r.json()
    books = result['data']
    return render(request, 'index.html', {'books': books})


def detail(request, pk):
    r = requests.get(f'{root}/get/{pk}/')
    result = r.json()
    if result['success'] is True:
        book = result['data']
        return render(request, 'detail.html', {'book': book})
    else:
        message = result['message']
        return render(request, 'result.html', {'message': message})


def search(request):
    return render(request, 'critic_reviews.html')

