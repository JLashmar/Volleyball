from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    PLAYER = 1
    COACH = 2
    CLUB_SECRETARY = 3
    CLUB_MEDIA = 4
    ADMIN = 5
    ROLE_CHOICES = (
        (PLAYER, 'player'),
        (COACH, 'coach'),
        (CLUB_SECRETARY, 'club secretary'),
        (CLUB_MEDIA, 'club media'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    #team = models.ManyToManyField(Team)
