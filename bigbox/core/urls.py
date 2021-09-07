from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import CategoryList, BoxList, ActivityList, CategoryDetail, BoxDetail, ActivityDetail
from core import views



urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<str:pk>/', CategoryDetail.as_view()),
    path('boxes/', BoxList.as_view()),
    path('boxes/<str:pk>/', BoxDetail.as_view()),
    path('activities/', ActivityList.as_view()),
    path('activities/<str:pk>/', ActivityDetail.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
