from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('profile/', views.profile_view, name='profile_detail'),
    path('edit/', views.edit_profile_view, name='edit_profile'),
]
