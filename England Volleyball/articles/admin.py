from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostArticle(admin.ModelAdmin):
    list_display = ('title', 'posted')
    prepopulated_fields = {'post_slug': ('title',)}
    # list_filter = ('post_category', )