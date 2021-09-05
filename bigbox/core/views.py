from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from core import serializers, models


class CategoryList(generics.ListAPIView):
	"""Obtener query de Categoria"""
	queryset = models.Category.objects.all()
	serializer_class = serializers.CategorySerializer


class CategoryDetail(generics.ListAPIView):
	serializer_class = serializers.CategorySerializer

	def get_queryset(self):
		slug = self.kwargs['pk']
		print(slug)
		return models.Category.objects.filter(slug=slug)




class BoxList(generics.ListAPIView):
	"""Obtener query de Box"""
	serializer_class = serializers.BoxSerializer
	queryset = models.Box.objects.all()


class BoxDetail(generics.ListAPIView):
	serializer_class = serializers.BoxSerializer

	def get_queryset(self):
		slug = self.kwargs['pk']
		print(slug)
		return models.Box.objects.filter(slug=slug)




class ActivityPagination(PageNumberPagination):
    page_size = 10


class ActivityList(generics.ListAPIView):
	"""Obtener query de Activity"""
	serializer_class = serializers.ActivitySerializer
	pagination_class = ActivityPagination
	queryset = models.Activity.objects.all()
	filter_backends = (DjangoFilterBackend, SearchFilter)
	filter_fields = ('category', 'reasons', 'slug')


class ActivityDetail(generics.ListAPIView):
	serializer_class = serializers.ActivitySerializer

	def get_queryset(self):
		slug = self.kwargs['pk']
		print(slug)
		return models.Activity.objects.filter(slug=slug)