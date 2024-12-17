from django.forms import ModelForm, Form, CharField, PasswordInput, TextInput, EmailInput
from django.contrib.auth.models import User
from .models import Book

class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={ 'placeholder': 'Username' }))
    password = CharField(widget=PasswordInput(attrs={ 'placeholder': 'Password' }))

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username': TextInput(attrs={ 'placeholder': 'Username' }),
            'email': EmailInput(attrs={ 'placeholder': 'Email' }),
            'password': PasswordInput(attrs={ 'placeholder': 'Password' })
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class Procurar(Form):
    nome = CharField(max_length=100, required=False, widget=TextInput(attrs={ 'id': 'busca' }))