from django.conf.urls import url
from blog_app import views

urlpatterns = [
    url(r'^about/$',views.AboutView.as_view(), name = 'about'),
    url(r'^$', views.PostListView.as_view(), name = 'post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name = 'post_detail'),
    url(r'^post/new/$', views.CreatPostView.as_view(), name = 'post_new'),
    url(r'^post/edit/(?P<pk>\d+)$', views.PostUpdateView.as_view(), name = 'post_edit'),
    url(r'^post/remove/(?P<pk>\d+)$', views.PostDeleteView.as_view(), name = 'post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name = 'post_draft_list'),

]