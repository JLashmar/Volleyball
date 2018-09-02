from django.contrib import admin
from .models import Sponsor, ClubSponsor, TeamSponsor, PlayerSponsor

# Register your models here.

admin.site.register(Sponsor)
admin.site.register(TeamSponsor)
admin.site.register(PlayerSponsor)


@admin.register(ClubSponsor)
class ClubSponsorAdmin(admin.ModelAdmin):
    list_display = ('club', 'sponsor')
    list_filter = ('club',)
