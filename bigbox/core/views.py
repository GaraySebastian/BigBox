from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from core import serializers, models

class CategorySerializerViewSet(viewsets.ModelViewSet):
	"""Obtener query de Categoria"""
	serializer_class = serializers.CategorySerializer
	queryset = models.Category.objects.all()


class BoxSerializerViewSet(viewsets.ModelViewSet):
	"""Obtener query de Box"""
	serializer_class = serializers.BoxSerializer
	queryset = models.Box.objects.all()


class ActivitySerializerViewSet(viewsets.ModelViewSet):
	"""Obtener query de Activity"""
	serializer_class = serializers.ActivitySerializer
	queryset = models.Activity.objects.all()