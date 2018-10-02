from django.db import models
from django.conf import settings
from .validators import validate_content
# Create your models here.



class Tweets(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    content     =   models.CharField(max_length=140, validators=[validate_content])
    updated     =   models.DateTimeField(auto_now=True)
    timestamp   =   models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    class Meta:
        verbose_name = "Tweet"
        verbose_name_plural = "Tweets"

    """ def clean(self,*args,**kwargs):
        content = self.content
        if content == "abc":
            raise ValidationError("Content cannot be abc")
        return super(Tweets,self).clean(*args,**kwargs) """