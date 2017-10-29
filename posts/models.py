from django.db import models
from django.urls import reverse
from django_twitter.user_messages.models import User
from django_twitter.comments.models import Comment


class Post(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(User)
    content = models.TextField()
    date_added = models.DateField()
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-view', kwargs={'pk': self.pk})




