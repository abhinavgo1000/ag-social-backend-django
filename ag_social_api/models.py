from django.db import models


class UserAuth(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateTimeField()

    def __str__(self):
        return self.first_name

