from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User, Book, Author, Reader


@admin.register(User)
class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    readonly_fields = ('last_login', 'date_joined')
    list_per_page = 10
    list_max_show_all = 100


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'page_amount', 'author', 'available_amount')
    list_per_page = 10
    list_max_show_all = 100


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'image')
    list_per_page = 10
    list_max_show_all = 100


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')
    list_per_page = 10
    list_max_show_all = 100
