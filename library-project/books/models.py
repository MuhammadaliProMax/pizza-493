from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=36)
  description = models.TextField()
  image = models.ImageField(upload_to="books")
  page_size = models.IntegerField()
  price = models.IntegerField()
  published_year = models.IntegerField()
  
  created_at = models.DateTimeField(auto_now_add=True)