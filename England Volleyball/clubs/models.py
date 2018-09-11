from django.db import models
from accounts.models import Profile
from rest_framework.reverse import reverse as api_reverse


class Club(models.Model):
    name = models.CharField(max_length=100, unique=False)
    club_slug = models.SlugField(max_length=100, unique=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api-clubs:club-rud', kwargs={'pk': self.pk}, request=request)


class Team(models.Model):
    name = models.CharField(max_length=100, unique=False)
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    logo = models.ImageField(null=True)
    MEN = 'Men'
    WOMEN = 'Women'
    MIXED = 'Mixed'
    GENDER_CHOICES = (
        (MEN, 'Men'),
        (WOMEN, 'Women'),
        (MIXED, 'Mixed'),
    )
    gender = models.CharField(
        max_length=5,
        choices=GENDER_CHOICES,
        default=MEN,
    )

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return '%s - %s' % (self.name, self.gender)

    def get_api_url(self, request=None):
        return api_reverse('api-clubs:team-rud', kwargs={'pk': self.pk}, request=request)
