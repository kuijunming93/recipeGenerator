from django.contrib import admin
from .models import GenerateType, Recipe, ImageType

# Register your models here.
admin.site.register(GenerateType)
admin.site.register(Recipe)
admin.site.register(ImageType)