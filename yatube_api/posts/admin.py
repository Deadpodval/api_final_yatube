from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('text', 'pub_date', 'author', 'image', 'group')
    empty_value_display = 'пусто'


@admin.register(Comment)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('author', 'post', 'text', 'created')
    empty_value_display = 'пусто'


@admin.register(Group)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description')
    empty_value_display = 'пусто'


@admin.register(Follow)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('user', 'following')
    empty_value_display = 'пусто'
