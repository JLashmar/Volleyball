from django.db import models
from sponsors.models import Sponsor
from accounts.models import Profile
from clubs.models import Team

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100, unique=False)
    sponsor_name = models.ForeignKey(Sponsor, on_delete=models.PROTECT, blank=True)
    league_contact = models.ForeignKey(Profile, on_delete=models.PROTECT, blank=True)


class LeagueTable(models.Model):
    year = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)


#class Membership(models.Model):
#    league_table = models.ForeignKey(LeagueTable, on_delete=models.PROTECT)
#    team = models.ForeignKey(Team, on_delete=models.PROTECT)


class LeagueTableData(models.Model):
    league = models.ForeignKey(LeagueTable, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team)
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
