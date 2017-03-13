from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0) #number of times post is viewed
    tag = models.CharField(max_length=30, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title