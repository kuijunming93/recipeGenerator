from django.db import models
from django.utils import timezone

# Create your models here.
class GenerateType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    imgPath = models.URLField(max_length=800, blank=True)
    description = models.CharField(max_length=200, blank=True)
    textPrompt = models.CharField(max_length=350, blank=True)
    imgPrompt = models.CharField(max_length=350, blank=True)
    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "imgPath": self.imgPath,
            "description": self.description,
            "textPrompt": self.textPrompt,
            "imgPrompt": self.imgPrompt
        })

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    content = models.CharField(max_length=3000, blank=True)
    imgPath = models.URLField(max_length=1000, blank=True)
    recipeType = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    imgType = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "imgPath": self.imgPath,
            "content": self.content,
            "recipeType": self.recipeType,
            "timestamp": self.timestamp
        })

class ImageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    imgPrompt = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "imgPrompt": self.imgPrompt
        })