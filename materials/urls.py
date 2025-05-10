from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_materials_view, name='study_materials'),
    path('upload/', views.upload_study_material_view, name='upload_study_material'),
    path('view/<int:pk>/', views.view_study_material, name='view_study_material'),
]
