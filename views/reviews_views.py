import requests
from django.shortcuts import render

from core.settings import API_URL as root
root += 'book_review'
test_user_id = 'ben123@gmail.com'


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
    user_id = request.GET.get('user_id')
    r = requests.get(
        f'{root}/get_critic_reviews/',
        params={'user_id': user_id},
    )
    data = r.json()
    books = data['data']
    return render(request, 'critic_reviews.html', {'books': books})


def edit(request):
    if request.method == 'GET':
        return render(request, 'edit_form.html')

    book_no = request.POST['book_no']
    title = request.POST['title']
    name = request.POST['name']
    comment = request.POST['comment']

    data = {
        'user_id': test_user_id,
        'title': title,
        'name': name,
        'comment': comment
    }

    r = requests.post(
        f'{root}/edit/{book_no}/',
        data=data
    )
    result = r.json()
    return render(request, 'result.html', {'message': result['message']})


def delete(request):
    if request.method == 'GET':
        return render(request, 'delete_form.html')

    book_no = request.POST['book_no']
    data = {
        'user_id': test_user_id
    }

    r = requests.post(
        f'{root}/delete/{book_no}/',
        data=data
    )
    result = r.json()
    return render(request, 'result.html', {'message': result['message']})

