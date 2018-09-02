from django.urls import path
from .views import SponsorAPIView, SponsorRudView

app_name = 'api-sponsors'

urlpatterns = [
    path('', SponsorAPIView.as_view(), name='sponsor-listcreate'),
    path('<int:pk>/', SponsorRudView.as_view(), name='sponsor-rud'),
]
