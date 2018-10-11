from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exist. Please choose another one.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
    else:
        return render(request, 'accounts/signup.html')


def login(request):

    state = "Please log in below..."
    username = password = ''

    next = ""

    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            state = "You're successfully logged in!"
            if next == "":
                return redirect('home')
            else:
                return redirect(next)
        else:
            state = "Your username and/or password were incorrect."

    return render(
        request,
        'accounts/login.html',
        {
        'state': state,
        'username': username,
        'next': next,
        },

    )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
