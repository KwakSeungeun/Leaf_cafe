import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def main(request):
    user = None
    if 'current_user' in request.session:
        user = User.getUser(request.session['current_user'])

    cafes = Cafe.getCafesByTag(request.GET.get('tag'))
    cafe_data = serializers.serialize('json', cafes, fields=('name', 'location', 'available_seat'))
    return render(request, 'main.html', {"cafe_data": cafe_data, 'user': user, 'tags':Tag.objects.all()})


def cafe_detail(request, cafe_id):
    tags = [t.name for t in Cafe.objects.filter(id=cafe_id).first().tags.all()]
    return HttpResponse(json.dumps(tags), content_type='application/json')


def cafe_comment(request, cafe_id):
    comments = [c for c in Comment.objects.filter(cafe_id=cafe_id).values()]
    return HttpResponse(json.dumps(comments), content_type='application/json')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        return do_signin(request)


def do_signin(request):
    user = User.getUserByLogin(request.POST['email'], request.POST['pass'])
    if user:
        request.session['current_user'] = user.user_id
        return redirect('/')
    else:
        return render(request, 'signin.html', {'message': '입력하신 정보를 다시 확인해주세요.'})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return do_signup(request)


def do_signup(request):
    input_precheck(request)

    user = create_user(request)
    if not user:
        return render(request, 'signup.html', {'message': '이미 가입된 아이디 이거나, 입력을 다시 확인해주세요.'})

    request.session['current_user'] = user.user_id
    return redirect('/')


def input_precheck(request):
    if request.POST['pass'] != request.POST['pass-repeat']: return None
    if 'name' not in request.POST: return None
    if 'email' not in request.POST: return None
    if 'pass' not in request.POST: return None
    if 'pass-repeat' not in request.POST: return None

    return render(request, 'signup.html', {'message': '입력을 다시 확인해주세요.'})


def create_user(request):
    try:
        user = User.objects.create(name=request.POST['name'], user_id=request.POST['email'],
                                   password=request.POST['pass'])
        user.save()
    except:
        return None

    return user


def signout(request):
    try:
        del request.session['current_user']
    except:
        pass
    return redirect('/')
