from django.db import models

from users.models import User


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.text[:25] + '...'


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='entries')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:25] + '...'

