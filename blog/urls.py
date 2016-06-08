from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^(?P<category_pk>\d+)/comments/new$', views.review_new, name='review_new'),
    url(r'^(?P<category_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.review_edit, name='review_edit'),
]