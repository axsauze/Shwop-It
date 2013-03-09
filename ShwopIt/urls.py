from django.conf.urls import patterns, include, url
from Shwopper import views
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^shwoplink/$', views.processShwopLink, name='processShwopLink'),
    url(r'^admin/', include(admin.site.urls)),
)

#Any override for userena views goes here:
urlpatterns += patterns('',
    url(r'^accounts/', include('userena.urls')),
)

#For Static media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

#Process redirect request
urlpatterns += patterns('',
    url(r'^(?P<code>\w+)/$', views.processRequest, name='processRequest'),
)