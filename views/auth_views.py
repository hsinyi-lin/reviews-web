import requests
from django.shortcuts import render, redirect

from core.settings import API_URL as root
root += 'auth'


def login(request):
    if 'user_id' in request.COOKIES:
        return redirect('/reviews/')
    if request.method == 'GET':
        return render(request, 'login_form.html')

    user_id = request.POST['user_id']
    pwd = request.POST['pwd']

    data = {
        'id': user_id,
        'pwd': pwd
    }

    r = requests.post(
        f'{root}/login/',
        data=data
    )

    result = r.json()
    if result['success'] is True:
        ret = redirect('/reviews/')
        ret.set_cookie('sessionid', result['sessionid'])
        ret.set_cookie('user_id', user_id)
        return ret
    else:
        return redirect('/login/')


def logout(request):
    r = requests.post(
        f'{root}/logout/',
        cookies={'sessionid': request.COOKIES['sessionid']}
    )

    ret = redirect('/login/')
    ret.delete_cookie('user_id')
    ret.delete_cookie('sessionid')
    return ret

