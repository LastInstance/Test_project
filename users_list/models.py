from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    def __str__(self):
        return self.username