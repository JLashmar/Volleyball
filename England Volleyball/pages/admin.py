from django.contrib import admin
from .models import PageCategory, Page
# Register your models here.


@admin.register(PageCategory)
class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'category_slug': ('title',)}
    # list_filter = ('post_category', )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    prepopulated_fields = {'page_slug': ('title',)}

    # list_filter = ('post_category', )
