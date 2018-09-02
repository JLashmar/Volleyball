from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey

from rest_framework.reverse import reverse as api_reverse


class Role(models.Model):
    role = models.CharField(max_length=255, default="none")

    def __str__(self):
        return self.role


class Position(models.Model):
    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="none")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    position = models.ManyToManyField(Position)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # need to add qualifications for coaches & and the dates they run out if applicable
    # need to add first aid qualifications & the dates they run out

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

    def get_api_url(self, request=None):
        return api_reverse('api-profiles:profile-rud', kwargs={'pk': self.pk}, request=request)
