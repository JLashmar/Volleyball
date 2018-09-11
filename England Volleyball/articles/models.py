from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import DateTimeField
from django.urls import reverse


from accounts.models import Profile
from clubs.models import Club, Team
from smart_selects.db_fields import ChainedForeignKey
from rest_framework.reverse import reverse as api_reverse


def get_upload_path(instance, filename):
    return "%s/%s" % (instance.club.name, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=False)
    post_slug = models.SlugField(max_length=100, unique=True)
    #team_a = models.ForeignKey('teams.Team', related_name='first_team', on_delete=models.CASCADE, blank=True, null=True)
    #team_b = models.ForeignKey('teams.Team', related_name='second_team', on_delete=models.CASCADE, blank=True, null=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=get_upload_path)
    image_credit = models.CharField(max_length=150, blank=True, null=True)
    #youtube_link = models.URLField(blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'club_slug': self.club.club_slug, 'post_slug': self.post_slug})

    def get_club_url(self):
        return reverse('articles:club', kwargs={'club_slug': self.club.club_slug})

    def get_api_url(self, request=None):
        return api_reverse('api-posts:post-rud', kwargs={'pk': self.pk}, request=request)


class Announcement(models.Model):
    message = models.TextField(max_length=250)
    # type = selector field. Select between "Club Announcement and an internal announcment"
    # club ID = request.user.club
    # email_list = no idea. However the email system should work needs to be intergrated into this.
