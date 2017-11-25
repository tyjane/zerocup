from django.db import models

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=10)
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     def register(self):
#         self.save()

class Memory(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    def post(self):
        self.save()
