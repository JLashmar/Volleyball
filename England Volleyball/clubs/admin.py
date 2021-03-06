from django.contrib import admin

from .models import Club, Team


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'club_slug': ('name',)}


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'club', 'gender')
    list_filter = ('club', 'gender')
