from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from newrelic import views
from django.conf.urls import include

urlpatterns = [
	url(r'^$', views.api_root),
	url(r'^newrelic/$', views.api_key_list.as_view()),
	url(r'^newrelic/(?P<pk>[0-9]+)/$', views.api_key_detail.as_view()),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#	url(r'^newrelic/(?P<pk>[0-9]+)/highlight/$', views.newrelicHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
