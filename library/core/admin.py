from django.contrib import admin
from .models import Book, Category

# Register your models here.

#REGISTERED THE MODEL HERE
admin.site.register(Book)
admin.site.register(Category)