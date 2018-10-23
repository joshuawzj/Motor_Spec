from django.db import models

# Create your models here.

class Users(models.Model):

    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name = models.CharField(max_length=128, unique = True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    sex = models.CharField(max_length = 32, choices = gender, default = 'Male')
    c_time = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name

class Meta:

    ordering = ['c_time']
    verbose_name = 'User'
    verbose_name_plural = 'User'
