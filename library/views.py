from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        print('HEY')
        form = LoginForm(request.POST)

        print(form.errors)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            print(user)

            if user != None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'login.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        print(form.errors)

        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)