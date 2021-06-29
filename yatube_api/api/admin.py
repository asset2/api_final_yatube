from django.contrib import admin

from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Comment, CommentAdmin)
