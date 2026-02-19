from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    # Hocanın "Azure Storage'dan görsel sunmalı" şartı için fotoğraf alanı:
    image = models.ImageField(upload_to='meals/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"