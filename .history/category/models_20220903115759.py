from distutils.command.upload import upload
from tabnanny import verbose
from tokenize import blank_re
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = "Categories"

        def get_url(self):
            

    def __str__(self):
        return self.category_name