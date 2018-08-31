from django.contrib import admin

from .models import Club, Team, Staff


@admin.register(Club)
class PostArticle(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Team)
class PostArticle(admin.ModelAdmin):
    list_display = ('name', 'club', 'gender')
    list_filter = ('club', 'gender')


@admin.register(Staff)
class PostArticle(admin.ModelAdmin):
    list_display = ('club', 'user', 'position')
    list_filter = ('club', 'position')
