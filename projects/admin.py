from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.category)
admin.site.register(models.project)
admin.site.register(models.task)
