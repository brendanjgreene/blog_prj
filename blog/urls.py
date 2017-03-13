from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.get_base),
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/top/$', views.top_lists),
]
