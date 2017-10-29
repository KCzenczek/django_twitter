from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserMessage(models.Model):
    sender = models.ForeignKey(
        User,
    )
    recipient = models.ForeignKey(
        User,
    )
    title = models.CharField(
        max_length=64,
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    date_sent = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return 'From: {}, Title: {}'.format(self.recipient.username, self.title)
