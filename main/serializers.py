from rest_framework import serializers
from .models import FoodType,Food,Comment

class FoodTypeSerializer(serializers.ModelSerializer):
    """Serializer for Food type."""
    class Meta:
        model = FoodType
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    """Serializer for Food type."""
    class Meta:
        model = Food
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment"""
    class Meta:
        model = Comment
        fields = '__all__'