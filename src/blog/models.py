from django.conf import settings
from django.db import models


# Create your models here.

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model): # blogpost_set -> queryset
    # id = models.IntegerField()
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
