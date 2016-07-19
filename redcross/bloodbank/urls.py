from django.conf.urls import url
from .views import *

urlpatterns=[
url(r'^$', home,name='bbhome'),
url(r'^about/', about,name='bbabout'),
url(r'^downloads/', downloads,name='downloads'),
url(r'^gallery/', gallery,name='bbgallery'),
url(r'^statistics/', statistics,name='statistics'),
url(r'^one/', one,name='1'),
url(r'^two/', two,name='2'),
url(r'^three/', three,name='3'),
url(r'^four/', four,name='4'),
url(r'^faq/', faq,name='faq'),
]