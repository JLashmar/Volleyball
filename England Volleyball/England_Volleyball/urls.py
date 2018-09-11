from django.conf import settings

from datetime import datetime
from django.conf.urls import url

from django.urls import include, path
from django.contrib import admin
admin.autodiscover()

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_schema_view(title='England Vollyball API')

from django.conf.urls.static import static


urlpatterns = [
    # web pages
    path('', include('articles.urls')),
    path('<slug:category_slug>', include('pages.urls')),
    # admin related things
    path('admin/', admin.site.urls),
    path('chaining/', include('smart_selects.urls')),
    # api additions
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('api-frontend/', include_docs_urls(title='England Vollyball API', public=False)),
    # api lists
    path('api/clubs/', include('clubs.api.urls')),
    path('api/posts/', include('articles.api.urls')),
    path('api/profiles/', include('accounts.api.urls')),
    path('api/leagues/', include('leagues.api.urls')),
    path('api/sponsors/', include('sponsors.api.urls')),
    path('api/auth/login/', obtain_jwt_token, name='api-login')
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
