from django.db import models

# Create your models here.


class Request(models.Model):
    message=models.TextField()

    def __str__(self):
        return f'{self.message}'