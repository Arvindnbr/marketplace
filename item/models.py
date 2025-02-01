from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'ProductCategories'

    def __str__(self):
        return self.name


class ProductItems(models.Model):
    category = models.ForeignKey(ProductCategory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='image_items', null=True, blank=True)
    is_sold = models.BooleanField(default=False,)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name