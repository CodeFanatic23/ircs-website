from django.conf.urls import url
from .views import *

urlpatterns=[
url(r'^$', home,name='bbhome'),
url(r'^about/', about,name='bbabout'),
url(r'^downloads/', downloads,name='downloads'),
url(r'^gallery/', gallery,name='bbgallery'),
url(r'^statistics/', statistics,name='statistics'),
]