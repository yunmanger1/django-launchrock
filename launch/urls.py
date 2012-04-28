from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'launch.views.signup', name='launch-signup'),
    url(r'^done/$', 'launch.views.done', name='launch-done'),
)
