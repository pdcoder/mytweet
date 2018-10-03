from rest_framework import serializers
from tweets.models import Tweets

class TweetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp'
        ]