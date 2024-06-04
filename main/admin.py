from django.contrib import admin
from .models import  FoodType, Food, Comment

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', )
    list_display_link = ('id', 'name')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food_type', 'price', 'ingredients')
    list_display_link = ('id', 'name', 'food_type')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'food', 'text', 'created')
    list_display_link = ('id', 'author', 'food')





















































































































































































































































