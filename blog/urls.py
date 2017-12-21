from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

]

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^home/$', views.home, name='home'),
    url(r'^notes/$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home'}, name='logout'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
