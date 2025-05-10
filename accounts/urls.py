from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('home/', views.home_view, name='home'),
    path('ai-chat/', views.ai_chat, name='ai_chat'),
    path('about/', views.about, name='about'),
]
