from django.db import models


class CountMessages(models.Model):
    count = models.IntegerField(default=0)