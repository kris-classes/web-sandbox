from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Video)
admin.site.register(models.Genre)
admin.site.register(models.Category)
admin.site.register(models.Action)