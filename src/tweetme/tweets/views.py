from django.shortcuts import render, get_object_or_404
from django.forms.utils import ErrorList
from .models import Tweets
from django.views.generic import ListView,DetailView, CreateView
from .forms import TweetModelForm
# Create your views here.


class TweetCreateView(CreateView):
    #queryset = Tweets.objects.all()
    template_name ='tweets/create_view_html'
    form_class = TweetModelForm
    success_url = "/tweet/create/"

    def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(TweetCreateView, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to continue'])
            return self.form_invalid(form)

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