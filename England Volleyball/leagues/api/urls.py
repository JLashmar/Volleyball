from django.urls import path
from .views import(
    LeagueAPIView, LeagueRudView,
    LeagueTableAPIView, LeagueTableRudView,
    LeagueTableDataAPIView, LeagueTableDataRudView
)

app_name = 'api-leagues'

urlpatterns = [
    # league
    path('league/', LeagueAPIView.as_view(), name='league-listcreate'),
    path('league/<int:pk>/', LeagueRudView.as_view(), name='league-rud'),
    # League Table
    path('league_table/', LeagueTableAPIView.as_view(), name='leaguetable-listcreate'),
    path('league_table/<int:pk>/', LeagueTableRudView.as_view(), name='leaguetable-rud'),
    # League Table Data
    path('league_table_data/', LeagueTableDataAPIView.as_view(), name='leaguetabledata-listcreate'),
    path('league_table_data/<int:pk>/', LeagueTableDataRudView.as_view(), name='leaguetabledata-rud'),
]
