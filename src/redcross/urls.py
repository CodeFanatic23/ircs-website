"""redcross URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from redcrossmain.views import *
from django.conf import settings
from django.conf.urls import include
from registration import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import password_reset_confirm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home,name='home'),
    url(r'^posts/', post,name='post'),
    url(r'^test/$', test,name='test'),
    url(r'^about/', about,name='about'),
    url(r'^membership/$', membership,name='membership'),
    url(r'^bloodbank/', include('bloodbank.urls'),name='bloodbank'),
    url(r'^volunteer/$', volunteer,name='volunteer'),
    url(r'^donate/$', donate,name='donate'),
    url(r'^upload/$',upload,name='upload'),
    url(r'^archive/$',archive,name='archive'),
    url(r'^gallery/$',gallery,name='gallery'),
    url(r'^learn/',learn,name='learn'),
    url(r'^stjohn/',stjohn,name='stjohn'),
    url(r'^icrc/',icrc,name='icrc'),
    url(r'^disastermanagement/',dm,name='dm'),
    url(r'^news/',news,name='news'),
    url(r'^rti/',rti,name='rti'),
    url(r'^forms',forms,name='forms'),
    url(r'^tenders/',tender,name='tender'),
    url(r'^careers/',career,name='career'),
    url(r'^newsletter/$',newsletter,name='newsletter'),
    url(r'^users/',include('userprofile.urls')),
    url(r'^events/',events,name='event'),
    url(r'^form/$',redcrossadmin,name='redcrossadmin'),
    # url(r'alerts/create/$',create_alert,name='create_alert'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
]

admin.site.site_header = 'Indian Red Cross WebPanel'
admin.site.site_title = 'Indian Red Cross Society'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += urlpatterns(
#         '',
#         url(
#             r'^media/(?P<path>.*)$',
#             'django.views.static.serve', {
#                 'document_root': settings.MEDIA_ROOT,
#             }
#         ),
#     )

urlpatterns += staticfiles_urlpatterns()