from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Book)
admin.site.register(models.Product)
admin.site.register(models.BookInstance)
admin.site.register(models.Status)