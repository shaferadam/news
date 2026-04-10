from django.contrib import admin
from .models import Article, Comment

class CommentInLine(admin.TabularInline): #Changed from StackedInLine
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,     #Added by Adam
    ]
    list_display = [
        "title",
        "body",
        "author",
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

