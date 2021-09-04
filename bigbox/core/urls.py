from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategorySerializerViewSet)
router.register('boxes', views.BoxSerializerViewSet)
router.register('activities', views.ActivitySerializerViewSet)


urlpatterns = [
    path('', include(router.urls))
]
