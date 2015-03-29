from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$',views.index),
        url(r'^about/$',views.about),
        url(r'^category/(?P<category_name_url>\w+)/$', views.category,name='category'),
        url(r'^add_category/$',views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_url>\w+)/add_page/$',views.add_page, name='add_page'),
        url(r'^register/$',views.register,name='register'),
        url(r'^login/$',views.user_login,name='login'),
        url(r'^restricted/$', views.restricted,name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^category/(?P<category_name>\w+)/likes/$', views.add_likes, name='category likes'),
        url(r'^category/(?P<category_name>\w+)/comment/$', views.add_comment, name="comment"),
        url(r'^user/user_details/$', views.user_details, name="user details"),
    )
