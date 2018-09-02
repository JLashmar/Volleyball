from django.db import models
from accounts.models import Profile
from clubs.models import Club, Team
from rest_framework.reverse import reverse as api_reverse


class Sponsor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    info = models.TextField(max_length=500, blank=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_api_url(self, request=None):
        return api_reverse('api-sponsors:sponsor-rud', kwargs={'pk': self.pk}, request=request)


class ClubSponsor(models.Model):
    club = models.ForeignKey(Club, on_delete=models.PROTECT)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    deal_end_date = models.DateField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.club, self.sponsor)

    def get_api_url(self, request=None):
        return api_reverse('api-sponsors:clubsponsor-rud', kwargs={'pk': self.pk}, request=request)


class TeamSponsor(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    deal_end_date = models.DateField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.team, self.sponsor)

    def get_api_url(self, request=None):
        return api_reverse('api-sponsors:teamsponsor-rud', kwargs={'pk': self.pk}, request=request)


class PlayerSponsor(models.Model):
    player = models.ForeignKey(Profile, on_delete=models.PROTECT)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    deal_end_date = models.DateField(blank=True)

    def __str__(self):
        return '%s - %s' % (self.player, self.sponsor)

    def get_api_url(self, request=None):
        return api_reverse('api-sponsors:playersponsor-rud', kwargs={'pk': self.pk}, request=request)
