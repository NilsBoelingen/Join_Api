from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JoinUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joined_date = models.DateField(auto_now_add=True)
    telefone = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=10)
    user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Task(models.Model):
    titel = models.CharField(max_length=200)
    task = models.TextField(blank=True, null=True)
    date = models.DateField()
    assignedTo = models.ManyToManyField(Contact, related_name='assignedTo', blank=True)
    urgency = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.titel

class Subtask(models.Model):
    content = models.CharField(max_length=200)
    checked = models.BooleanField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return self.titel
    