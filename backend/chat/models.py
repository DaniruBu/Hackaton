from django.db import models


class MessageGPT(models.Model):
    role = models.CharField(max_length=30)
    text = models.TextField()


class HobbyGPT(models.Model):
    name = models.CharField(max_length=30)


class RequestGetOptimalRouteChat(models.Model):
    text = models.TextField()

class Vershina(models.Model):
    description = models.ForeignKey("Des", on_delete=models.CASCADE)


class Des(models.Model):
    description = models.TextField()


class Vetka(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    len = models.IntegerField()
    description = models.ForeignKey(Des, on_delete=models.CASCADE)
