from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_age = models.IntegerField()
    user_birthdate = models.DateField()

    def __str__(self):
        return f'Apelido: {self.user_nickname} | Email: {self.user_email}'