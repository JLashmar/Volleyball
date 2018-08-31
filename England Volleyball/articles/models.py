from django.conf import settings
from django.db import models
from django.db.models.fields import DateTimeField

from rest_framework.reverse import reverse as api_reverse

# def get_upload_path(instance, filename):
# return "%s/%s" % (instance.post_category.name, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=False)
    post_slug = models.SlugField(max_length=100, unique=True)
    #team_a = models.ForeignKey('teams.Team', related_name='first_team', on_delete=models.CASCADE, blank=True, null=True)
    #team_b = models.ForeignKey('teams.Team', related_name='second_team', on_delete=models.CASCADE, blank=True, null=True)
    short_description = models.CharField(max_length=150, blank=True, null=True)
    body = models.TextField()
    #image = models.ImageField(blank=True, null=True, upload_to=get_upload_path)
    #image_credit = models.CharField(max_length=150, blank=True, null=True)
    #youtube_link = models.URLField(blank=True, null=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse('articles:detail', kwargs={'sport_slug': self.post_category.sport_slug, 'post_slug': self.post_slug})

    def get_api_url(self, request=None):
        return api_reverse('api-posts:post-rud', kwargs={'pk': self.pk}, request=request)
