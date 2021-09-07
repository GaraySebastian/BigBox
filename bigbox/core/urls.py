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
]
