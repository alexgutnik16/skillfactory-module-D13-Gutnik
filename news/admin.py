from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment, CategoryUser


class PostAdmin(admin.ModelAdmin):
    list_display = ('heading', 'creation_date')
    search_fields = ('heading',)


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(CategoryUser)
