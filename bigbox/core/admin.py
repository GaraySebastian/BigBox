from django.contrib import admin
from core import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BoxResource(resources.ModelResource):
	class Meta:
		model = models.Box

class BoxAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['id', 'name']
	resource_class = BoxResource



class BoxImageResource(resources.ModelResource):
	class Meta:
		model = models.BoxImage

class BoxImageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['id']
	list_display = ['id', 'box']
	resource_class = BoxImageResource




class ActivityResource(resources.ModelResource):
	class Meta:
		model = models.Activity

class ActivityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['id', 'name']
	resource_class = ActivityResource



class ActivityImageResource(resources.ModelResource):
	class Meta:
		model = models.ActivityImage

class ActivityImageAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['id']
	list_display = ['id', 'activity']
	resource_class = ActivityImageResource



class CategoryResource(resources.ModelResource):
	class Meta:
		model = models.Category

class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['id', 'name']
	resource_class = CategoryResource




class ReasonResource(resources.ModelResource):
	class Meta:
		model = models.Reason

class ReasonAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['id', 'name']
	resource_class = ReasonResource




admin.site.register(models.Box, BoxAdmin)
admin.site.register(models.BoxImage, BoxImageAdmin)
admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.ActivityImage, ActivityImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Reason, ReasonAdmin)
