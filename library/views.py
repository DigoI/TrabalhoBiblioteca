from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
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

def book_details(request, book_id):

    livro = Book.objects.get(id=book_id)

    context = {
        "livro": livro
    }

    return render(request, 'book.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = BookForm()

    context = {
        'form': form
    }

    return render(request, 'create_book.html', context)

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()

            return redirect('index')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form
    }

    return render(request, 'create_book.html', context)

def book_list(request):
    books_list = Book.objects.all()
    form = Procurar(request.GET or None)
    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        if nome:
            books_list = books_list.filter(nome__icontains=nome)
    paginator = Paginator(books_list, 6)

    page = request.GET.get('page', 1)

    try:
        books = paginator.get_page(page)
    except:
        books = paginator.get_page(1)

    context = {
        'books': books,
        'form': form
    }

    return render(request, 'book_list.html', context)

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()

    return redirect('index')

def categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render (request, 'categorias.html', context)

def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    books_list = Book.objects.all().filter(categoria=categoria)
    form = Procurar(request.GET or None)
    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        if nome:
            books_list = books_list.filter(nome__icontains=nome)
    paginator = Paginator(books_list, 6)

    page = request.GET.get('page', 1)

    try:
        books = paginator.get_page(page)
    except:
        books = paginator.get_page(1)

    context = {
        'books': books,
        'form': form
    }

    return render(request, 'book_list.html', context)

def usuario(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'usuario.html', context)

def sair(request):
    logout(request)
    return redirect('index')
