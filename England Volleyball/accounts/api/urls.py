from django.urls import path
from .views import ProfileAPIView, ProfileRudView

app_name = 'api-profiles'

urlpatterns = [
    path('', ProfileAPIView.as_view(), name='profile-listcreate'),
    path('<int:pk>/', ProfileRudView.as_view(), name='profile-rud'),
]
