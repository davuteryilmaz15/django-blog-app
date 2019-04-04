from django.contrib import admin

from .models import Article, Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title", "content"]
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title", "author"]
    list_filter = ["created_date"]

    class Meta:
        model = Article

#admin.site.register(Article, ArticleAdmin)
#admin.site.register(Article)

admin.site.register(Comment)