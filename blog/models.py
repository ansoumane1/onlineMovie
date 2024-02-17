from django.db import models

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  date = models.DateField()
  def __str__(self):
    return self.title