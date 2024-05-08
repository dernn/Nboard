from board.models import Category, Comment, Post, User

from django.contrib import admin

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
