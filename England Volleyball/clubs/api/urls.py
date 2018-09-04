from django.urls import path
from .views import(
    ClubAPIView, ClubRudView,
    TeamAPIView, TeamRudView,
)

app_name = 'api-clubs'

urlpatterns = [
    # clubs
    path('club/', ClubAPIView.as_view(), name='club-listcreate'),
    path('club/<int:pk>/', ClubRudView.as_view(), name='club-rud'),
    # team
    path('team/', ClubAPIView.as_view(), name='team-listcreate'),
    path('team/<int:pk>/', ClubRudView.as_view(), name='team-rud'),
]
