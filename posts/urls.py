from django.conf.urls import url
from django_twitter.posts import views


urlpatterns = [
    url(r'^post-view/(?P<pk>(\d)+)', views.PostView.as_view(), name="post-view"),
    url(r'^post-list/(?P<pk>(\d)+)', views.PostListView.as_view(), name="post-list"),
]
