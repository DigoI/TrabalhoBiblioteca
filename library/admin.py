from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']
    search_fields = ['nome']

admin.site.register(Autor)
admin.site.register(Categoria)