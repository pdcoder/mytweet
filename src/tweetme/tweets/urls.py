from .views import  TweetCreateView, TweetDetailView, TweetListView, TweetUpdateView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name="list"),
    url(r'^create/', CreateListView.as_view(), name="create"),
    url(r'^(?<pk>\d+)/$', TweetDetailView.as_view(), name="detail"),
]
