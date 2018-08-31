from django.contrib import admin

from .models import Profile, Role, Position

admin.site.register(Role)
admin.site.register(Position)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'club')
    list_filter = ('club', 'role')
