from django.urls import path
from .views import(
    SponsorAPIView, SponsorRudView,
    ClubSponsorAPIView, ClubSponsorRudView,
    TeamSponsorAPIView, TeamSponsorRudView,
    PlayerSponsorAPIView, PlayerSponsorRudView,
)

app_name = 'api-sponsors'

urlpatterns = [
    path('sponsor/', SponsorAPIView.as_view(), name='sponsor-listcreate'),
    path('sponsor/<int:pk>/', SponsorRudView.as_view(), name='sponsor-rud'),
    # clubs
    path('club/', ClubSponsorAPIView.as_view(), name='clubsponsor-listcreate'),
    path('club/<int:pk>/', ClubSponsorRudView.as_view(), name='clubsponsor-rud'),
    # team
    path('team/', ClubSponsorAPIView.as_view(), name='teamsponsor-listcreate'),
    path('team/<int:pk>/', ClubSponsorRudView.as_view(), name='teamsponsor-rud'),
    # player
    path('player/', ClubSponsorAPIView.as_view(), name='playersponsor-listcreate'),
    path('player/<int:pk>/', ClubSponsorRudView.as_view(), name='playersponsor-rud'),
]
