from django.contrib import admin

# Register your models here.
from .models import ProductCategory, ProductItems


admin.site.register(ProductCategory)
admin.site.register(ProductItems)