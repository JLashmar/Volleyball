"""
Definition of urls for England_Volleyball.
"""

from datetime import datetime
from django.conf.urls import url

from django.urls import include, path
from django.contrib import admin
admin.autodiscover()

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    # api additions
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='My API title',
                                    authentication_classes=[],
                                    permission_classes=[]))

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

]
