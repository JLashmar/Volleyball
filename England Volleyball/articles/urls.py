from django.conf.urls import url, include
from django.urls import path
from .views import IndexView

app_name = 'articles'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
