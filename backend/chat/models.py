from django.db import models


class MessageGPT(models.Model):
    role = models.CharField(max_length=30)
    text = models.TextField()
