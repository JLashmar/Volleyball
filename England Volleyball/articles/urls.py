from django.conf.urls import url, include
from django.urls import path
from .views import IndexView, DetailView, ClubView
from . import views

app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:club_slug>', ClubView.as_view(), name='club'),
    path('<slug:club_slug>/<slug:post_slug>', DetailView.as_view(), name='detail'),
]
