from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Hobby(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    skills = models.ManyToManyField("Skill", blank=True, related_name='hobby')

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    hobbies = models.ManyToManyField("Hobby", blank=True)
    skills = models.ManyToManyField("Skill", blank=True)
    link = models.URLField(blank=True)
    events = models.ManyToManyField("Events", blank=True)
    schedule = models.TextField(blank=True)


class TypeImportance(models.Model):
    name = models.CharField(max_length=30)
    importance = models.IntegerField()

    def __str__(self):
        return self.name


class TypeEvent(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)
    hobbies = models.ManyToManyField("Hobby", blank=True)
    skills = models.ManyToManyField("Skill", blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    type_importance = models.ForeignKey(TypeImportance, on_delete=models.CASCADE, related_name="events", null=True, blank=True)
    type_event = models.ForeignKey(TypeEvent, on_delete=models.CASCADE, related_name="events", null=True, blank=True)
    social_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    hobbies = models.ManyToManyField("Hobby")

    def __str__(self):
        return self.name
class User(AbstractUser):
    hobbies = models.ManyToManyField(Hobby)
    gender = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    groups = models.TextField()
    direction = models.TextField()
    communication_group = models.TextField()
    military_enlistment_office = models.TextField()
    date_of_birth = models.DateField(null=True)
    type_event = models.ManyToManyField(TypeEvent)
    type_importance = models.ManyToManyField(TypeImportance)
    nonresident = models.BooleanField(default=False)


class Place(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    type_integer = models.IntegerField()


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    type_integer = models.IntegerField()
    subject_integer = models.IntegerField()


class Schedule(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    type_integer = models.IntegerField()
    type_integer_id = models.IntegerField()
