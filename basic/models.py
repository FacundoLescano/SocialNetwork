from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings


# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=100)
#     age = models.IntegerField(default=0)
#     email = models.EmailField(max_length=50)

#     def __str__(self):
#         return self.username


class Publication(models.Model):
    users_publication = models.ForeignKey(User, on_delete=models.CASCADE)
    #users_publication = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    time_create = models.DateTimeField("publication published")

    def __str__(self):
        return self.title


class Friend(models.Model):
    # La ForeighKey por la que hacemos referencia.
    id_user_reference = models.ForeignKey(User, on_delete=models.CASCADE)
    # id del amigo que inicio el follow
    id_friend = models.IntegerField(default=0)
    # username del amigo que inicio el follow
    username_friend = models.CharField(max_length=100)

    def __str__(self):
        return self.username_friend