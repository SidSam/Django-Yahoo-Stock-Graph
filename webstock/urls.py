from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^goc/(?P<comp_name>[a-zA-Z\.]+)/(?P<date>[0-9]+)$', views.goc, name = 'goc'),
	url(r'^goc_range/(?P<comp_name>[a-zA-Z\.]+)/(?P<startD>[0-9]+)/(?P<endD>[0-9]+)$', views.goc_range, name = 'goc_range')
]