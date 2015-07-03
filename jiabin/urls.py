from django.conf.urls import patterns, include, url
# from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',

    #url(r'^index/$', 'jiabin.views.jiabin_list_index', name='home1'),
    #url(r'^index/(?P<page>[\d]+)/$', 'jiabin.views.jiabin_list_index', name='home'),
    #url(r'^index/guest/$', 'jiabin.views.jiabin_guest_index', name='home'),
    url(r'^guest_invitation/(?P<page>[\d]+)/$', 'jiabin.views.jiabin_guest_invitation', name='home'),
    url(r'^Search_guest/$', 'jiabin.views.Search_guest', name='home'),
    url(r'^$', 'jiabin.views.cat_guest', name='home'),
    url(r'^jiabin_cat_list_index/(?P<cat_n>[\d]+)/(?P<page>[\d]+)/', 'jiabin.views.jiabin_cat_list_index', name='home'),
    url(r'^send_guest_invitation', 'jiabin.views.send_guest_invitation', name='home'),
    url(r'^Search_guest/(?P<page>[\d]+)/', 'jiabin.views.Search_guest', name='home'),
    url(r'^apply_guest/$','jiabin.views.apply_guest', name='home'),
    url(r'^apply_guest_send/$','jiabin.views.apply_guest_send', name='home'),

)
