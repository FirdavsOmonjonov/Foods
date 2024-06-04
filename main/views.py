from django.shortcuts import render
from rest_framework import viewsets
from .models import FoodType,Comment, Food
from rest_framework import permissions
from .serializers import FoodTypeSerializer,FoodSerializer,CommentSerializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.

class FoodTypeView(viewsets.ModelViewSet):
    """View set for Food type."""
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class FoodView(viewsets.ModelViewSet):
    """View set for Food type."""
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class CommentView(viewsets.ModelViewSet):
    """View set for Commet."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]