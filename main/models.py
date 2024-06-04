from django.db import models
from rest_framework.authtoken.admin import User

# Create your models here.
class FoodType(models.Model):
    """Model for Food Type"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    """Model for Food"""
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    ingredients = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Model for Comment"""
    text = models.CharField(max_length=100)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text