from django.db import models


class MessageGPT(models.Model):
    role = models.CharField(max_length=30)
    text = models.TextField()


class HobbyGPT(models.Model):
    name = models.CharField(max_length=30)
