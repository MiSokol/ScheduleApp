from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=100)

    def __str__(self):
        return str(self.login)

class Task(models.Model):
    name = models.CharField(max_length=250)
    deadline = models.DateTimeField()
    time = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
