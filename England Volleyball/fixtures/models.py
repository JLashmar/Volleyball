from django.db import models
from sponsors.models import Sponsor
from accounts.models import Profile
from clubs.models import Team
from leagues.models import League

from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from rest_framework.reverse import reverse as api_reverse


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.PROTECT)
    date = models.DateTimeField()
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='team_b')

    def __str__(self):
        return '%s - %s' % (self.team_a, self.team_b)


class MatchData(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='test_team_a', default=None)
    team_b = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='test_team_b', default=None)
    team_a_squad = ChainedManyToManyField(
        Profile,
        verbose_name='a_squad',
        chained_field="team_a",
        chained_model_field="team",
        horizontal=True,
        related_name='team_a_squad')
    team_b_squad = ChainedManyToManyField(
        Profile,
        verbose_name='b_squad',
        chained_field="team_b",
        chained_model_field="team",
        horizontal=True,
        related_name='team_b_squad')

    def __str__(self):
        return self.match


class Continent(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    country = ChainedForeignKey(
        Country,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        sort=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)

    def __str__(self):
        return '%s - %s' % (self.continent, self.country)

# more test


class Publication(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Writer(models.Model):
    name = models.CharField(max_length=255)
    publications = models.ManyToManyField('Publication', blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    writer = ChainedManyToManyField(
        Writer,
        verbose_name='writer',
        chained_field="publication",
        chained_model_field="publications",
        horizontal=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
