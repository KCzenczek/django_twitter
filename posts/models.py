from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from comments.models import Comment

User = get_user_model()


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




