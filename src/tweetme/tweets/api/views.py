from rest_framework import generics
from .serializers import TweetModelSerializer
from tweets.models import Tweets

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    
    def get_queryset(self):
        return Tweets.objects.all()