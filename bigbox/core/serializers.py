from rest_framework import serializers
from core import models

class CategorySerializer(serializers.ModelSerializer):
	"""Serializa categoria"""
	class Meta:
		model = models.Category
		fields = '__all__'


class BoxSerializer(serializers.ModelSerializer):
	"""Serializa box"""
	class Meta:
		model = models.Box
		fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
	"""Serializa activity"""
	class Meta:
		model = models.Activity
		fields = '__all__'

