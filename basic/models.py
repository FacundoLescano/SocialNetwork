from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)
#     age = models.IntegerField(default=0)
#     email = models.EmailField(max_length=50)

#     def __str__(self):
#         return self.username


class Publication(models.Model):
    users_publication = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    time_create = models.DateTimeField("publication published")

    def __str__(self):
        return self.title