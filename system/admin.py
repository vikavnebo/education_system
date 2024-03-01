from django.contrib import admin

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', 'price', 'release', 'min_users_number', 'max_users_number')
	list_editable = ('author', 'price', 'release', 'min_users_number', 'max_users_number')
	list_filter = ('author',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
	list_display = ('name', 'product_id')
	list_filter = ('product_id',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	list_display_links = ('first_name', 'last_name', 'email')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'product_id')
	list_filter = ('product_id',)
