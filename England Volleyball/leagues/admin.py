from django.contrib import admin

from .models import League, LeagueTable, LeagueTableData
# Register your models here.


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name', 'sponsor_name', 'age_group', 'gender')
    list_filter = ('sponsor_name', 'age_group', 'gender')


@admin.register(LeagueTable)
class LeagueTableAdmin(admin.ModelAdmin):
    list_display = ('league', 'year')
    list_filter = ('league', 'year')


@admin.register(LeagueTableData)
class LeagueTableDataAdmin(admin.ModelAdmin):
    list_display = ('league', 'team')
    list_filter = ('league',)
