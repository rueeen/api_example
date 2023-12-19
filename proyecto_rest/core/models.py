from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
