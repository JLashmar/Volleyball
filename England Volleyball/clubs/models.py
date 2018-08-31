from django.db import models
from accounts.models import Profile
# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=100, unique=False)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    post_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=False)
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
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
        return self.name


class Staff(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, unique=False)
