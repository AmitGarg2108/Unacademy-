from django.urls import path
from . import views

urlpatterns = [
    path('daily/', views.daily_quiz_view, name='daily_quiz'),
    path('subject/<str:subject>/class/<str:class_level>/', views.quizzes_by_subject_class, name='quizzes_by_subject_class'),
    path('<int:quiz_id>/', views.quiz_detail_view, name='quiz_detail'),
    path('create/class10/science/', views.run_create_class10_science_quiz, name='create_class10_science_quiz'),
    path('create/class10/math/', views.run_create_class10_math_quiz, name='create_class10_math_quiz'),
    path('create/class10/english/', views.run_create_class10_english_quiz, name='create_class10_english_quiz'),
    path('create/class12/math/', views.run_create_class12_math_quiz, name='create_class12_math_quiz'),
    path('create/class12/science/', views.run_create_class12_science_quiz, name='create_class12_science_quiz'),
    path('create/class12/english/', views.run_create_class12_english_quiz, name='create_class12_english_quiz'),
]
