# models/subcategory.py

from django.db import models
from .category import Category

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)

    # other fields...
    @staticmethod
    def get_all_subcategories():
        return Subcategory.objects.all()

    def __str__(self):
        return self.name

