
from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_lectures_view, name='video_lectures'),
    path('view/<int:pk>/', views.video_lecture_detail_view, name='video_lecture_detail'),
]
