from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_base),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/top/$', views.top_lists),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post),
]
