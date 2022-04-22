from django.db import models

# Create your models here.
class Lesson(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Week = models.CharField(max_length=100, null=True, blank=True)
    Nyu = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.Name