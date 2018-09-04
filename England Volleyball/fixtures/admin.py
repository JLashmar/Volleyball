from django.contrib import admin
from .models import Match, MatchData, Continent, Country, Location

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location)


@admin.register(Match)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('league',)
    list_filter = ('league',)


@admin.register(MatchData)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('match',)
