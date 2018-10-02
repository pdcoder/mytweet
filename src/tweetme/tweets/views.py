from django.shortcuts import render
from .models import Tweets
from django.views.generic import ListView,DetailView

# Create your views here.


class TweetDetailView(DetailView):
    queryset = Tweets.objects.all()

    def get_object(self):
        return Tweets.objects.get(id=1)

class TweetListView(ListView):
    queryset = Tweets.objects.all()


def tweet_detail_view(request, id=1):
    obj = Tweets.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweets.objects.all()
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list": queryset
    }
    return render(request,"tweets/list_view.html", context)