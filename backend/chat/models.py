from django.db import models


class MessageGPT(models.Model):
    role = models.CharField(max_length=30)
    text = models.TextField()


class HobbyGPT(models.Model):
    name = models.CharField(max_length=30)


class RequestGetOptimalRouteChat(models.Model):
    text = models.TextField()


class Vershina(models.Model):
    description = models.TextField()


class Vetka(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    len = models.IntegerField()
    description = models.TextField()


class State(models.Model):
    state = models.IntegerField(default=0)
    start_point = models.TextField(null=True, blank=True)
    end_point = models.TextField(null=True, blank=True)


class StateMessanger(models.Model):
    state = models.IntegerField(default=0)
