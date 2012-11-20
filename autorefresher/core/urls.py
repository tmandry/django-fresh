from django.conf.urls import patterns, url


urlpatterns = patterns('autorefresher.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^refresher/$', 'refresher', name='refresher'),
)
