from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from smart_selects.db_fields import ChainedForeignKey


class Role(models.Model):
    PLAYER = 1
    ADMINISTRATOR = 2
    OFFICAL = 3
    ROLE_CHOICES = (
        (PLAYER, 'Player'),
        (ADMINISTRATOR, 'Administrator'),
        (OFFICAL, 'Offical'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Position(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    COACH = 'Coach'
    PRESS_OFFICER = 'Press Officer'
    REFEREES = 'Referees'
    WING_SPIKER = 'Wing Spiker'
    ATTACKER = 'Attacker'
    SETTER = 'Setter'
    CENTRE = 'Centre'
    LIBERO = 'Libero'
    DEFENSIVE_SPECIALIST = 'Defensive Specalist'
    POSITION_CHOICES = (
        (COACH, 'Coach'),
        (PRESS_OFFICER, 'Press Officer'),
        (REFEREES, 'Referees'),
        (WING_SPIKER, 'Wing Spiker'),
        (ATTACKER, 'Attacker'),
        (SETTER, 'Setter'),
        (CENTRE, 'Centre'),
        (LIBERO, 'Libero'),
        (DEFENSIVE_SPECIALIST, 'Defensive Specalist'),
    )
    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        default=COACH,
    )

    def __str__(self):
        return self.position


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default="1")
    position = ChainedForeignKey(
        Position,
        chained_field="role",
        chained_model_field="role",
        show_all=False,
        auto_choose=True,
        sort=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
