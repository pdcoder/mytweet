from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

def validate_content(value):
    content = value
    if content == "abc":
         raise ValidationError("Content cannot be abc")
    return value

class Tweets(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    content     =   models.CharField(max_length=140)
    updated     =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    """ def clean(self,*args,**kwargs):
        content = self.content
        if content == "abc":
            raise ValidationError("Content cannot be abc")
        return super(Tweets,self).clean(*args,**kwargs) """