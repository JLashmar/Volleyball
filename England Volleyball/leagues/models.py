from django.db import models
from sponsors.models import Sponsor
from accounts.models import Profile
from clubs.models import Team
from rest_framework.reverse import reverse as api_reverse


# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100, unique=False)
    sponsor_name = models.ForeignKey(Sponsor, on_delete=models.PROTECT, blank=True)
    league_contact = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True)
    SENIOR = 'Senior'
    UNDER_TWENTYTHREE = 'U23'
    UNDER_TWENTYONE = 'U21'
    UNDER_TWENTY = 'U20'
    UNDER_EIGHTEEN = 'U18'
    UNDER_SEVENTEEN = 'U17'
    UNDER_SIXTEEN = 'U16'
    GENDER_CHOICES = (
        (SENIOR, 'Senior'),
        (UNDER_TWENTYTHREE, 'U23'),
        (UNDER_TWENTYONE, 'U21'),
        (UNDER_TWENTY, 'U20'),
        (UNDER_EIGHTEEN, 'U18'),
        (UNDER_SEVENTEEN, 'U17'),
        (UNDER_SIXTEEN, 'U16'),
    )
    age_group = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default=SENIOR,
    )
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

    def __str__(self):
        return '%s - %s' % (self.name, self.gender)

    def get_api_url(self, request=None):
        return api_reverse('api-leagues:league-rud', kwargs={'pk': self.pk}, request=request)


class LeagueTable(models.Model):
    year = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return '%s - %s' % (self.league, self.year)

    def get_api_url(self, request=None):
        return api_reverse('api-leagues:leaguetable-rud', kwargs={'pk': self.pk}, request=request)


# class Membership(models.Model):
#    league_table = models.ForeignKey(LeagueTable, on_delete=models.PROTECT)
#    team = models.ForeignKey(Team, on_delete=models.PROTECT)


class LeagueTableData(models.Model):
    league = models.ForeignKey(LeagueTable, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default="1")
    wins = models.IntegerField()
    loss = models.IntegerField()
    draw = models.IntegerField()
    sf = models.IntegerField()
    sa = models.IntegerField()
    sq = models.IntegerField()
    pf = models.IntegerField()
    pa = models.IntegerField()
    pe = models.IntegerField()
    pq = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.league, self.team)

    def get_api_url(self, request=None):
        return api_reverse('api-leagues:leaguetabledata-rud', kwargs={'pk': self.pk}, request=request)
