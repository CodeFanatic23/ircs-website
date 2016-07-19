from django.conf.urls import patterns ,include, url
from .views import user_profile


urlpatterns = patterns('',
	url(r'^profile/$',user_profile),
	)