from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.utils import ErrorList
from .models import Tweets
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .forms import TweetModelForm
from .mixin import FormUserNeededList
# Create your views here.


class TweetCreateView(FormUserNeededList, CreateView):
    #queryset = Tweets.objects.all()
    template_name ='tweets/create_view_html'
    form_class = TweetModelForm
    success_url = "/tweet/create/"
    login_url = '/login/'

class TweetUpdateView(LoginRequiredMixin,UpdateView):
    queryset         =   Tweets.objects.all()
    form_class       =   TweetModelForm
    template_name    =   'tweet/update_view.html'
    success_url      =   '/tweet/'

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