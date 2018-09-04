from django.contrib import admin
from .models import Match, MatchData, Continent, Country, Location, Publication, Writer, Book

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Location)

# book stuff

admin.site.register(Publication)
admin.site.register(Writer)
admin.site.register(Book)


@admin.register(Match)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('league',)
    list_filter = ('league',)


@admin.register(MatchData)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('match',)
