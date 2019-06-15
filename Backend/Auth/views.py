from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def intro(request):
    return render(request, 'Auth/intro.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            newUser = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, newUser)
            return redirect('home')
            
    #request.get일때 오류처리를 하거나 signup전용 웹페이지로 코딩할수도 있다.
    else:
        return redirect('Auth:intro')

def signin(request):
    if request.method == 'POST':
        #request.GET.get('next')를 통해 로그인후에 띄울 웹페이지를 제어한다.
        next=request.GET.get('next')
        user = auth.authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            auth.login(request, user)
            if next == '':
                return redirect('home')
            else:
                return redirect(next)
        elif next == '':
            return redirect('home')
        else:
            return redirect('/?next=' + next)
    #request.get일때 오류처리를 하거나 signin전용 웹페이지로 코딩할수도 있다.
    else:
        return redirect('home')

def signout(request):
    auth.logout(request)
    return redirect('Auth:intro')
