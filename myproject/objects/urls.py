from django.urls import path
from . import views

urlpatterns = [
    path('', views.object_list, name='object_list'),
    path('object/<int:object_id>/', views.object_detail, name='object_detail'),
]