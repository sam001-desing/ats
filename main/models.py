from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_application = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return f'Applied: {self.position} on {self.created_at}.'