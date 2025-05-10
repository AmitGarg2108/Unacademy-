from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Quiz
from django.utils.timezone import now
from django.http import HttpResponse
import sys

def staff_member_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_active and u.is_staff)(view_func)
    return decorated_view_func

@login_required
def daily_quiz_view(request):
    today = now().date()
    quiz = Quiz.objects.filter(date=today).first()
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/daily_quiz.html', {'quiz': quiz, 'quizzes': quizzes})

@login_required
def quizzes_by_subject_class(request, subject, class_level):
    quizzes = Quiz.objects.filter(subject__iexact=subject, class_level=class_level)
    return render(request, 'quizzes/quizzes_by_subject_class.html', {'quizzes': quizzes, 'subject': subject, 'class_level': class_level})

@login_required
def quiz_detail_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        total_questions = quiz.questions.count()
        correct_answers = 0
        user_answers = {}
        for question in quiz.questions.all():
            selected_option = request.POST.get(f'question_{question.id}')
            user_answers[question.id] = int(selected_option) if selected_option else None
            if selected_option and int(selected_option) == question.correct_option:
                correct_answers += 1
        score = correct_answers

        # Save the score to UserQuizScore
        from profiles.models import UserQuizScore
        UserQuizScore.objects.create(user=request.user, quiz=quiz, score=score)

        return render(request, 'quizzes/quiz_detail.html', {
            'quiz': quiz,
            'score': score,
            'total_questions': total_questions,
            'user_answers': user_answers,
            'submitted': True
        })
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz})

@login_required
@staff_member_required
def run_create_class10_science_quiz(request):
    from quizzes.scripts.create_class10_science_quiz import create_class10_science_quiz
    create_class10_science_quiz()
    return HttpResponse("Class 10 Science Quiz created successfully.")

@login_required
@staff_member_required
def run_create_class10_math_quiz(request):
    from quizzes.scripts.create_class10_math_quiz import create_class10_math_quiz
    create_class10_math_quiz()
    return HttpResponse("Class 10 Math Quiz created successfully.")

@login_required
@staff_member_required
def run_create_class10_english_quiz(request):
    from quizzes.scripts.create_class10_english_quiz import create_class10_english_quiz
    create_class10_english_quiz()
    return HttpResponse("Class 10 English Quiz created successfully.")

@login_required
@staff_member_required
def run_create_class12_math_quiz(request):
    from quizzes.scripts.create_class12_math_quiz import create_class12_math_quiz
    create_class12_math_quiz()
    return HttpResponse("Class 12 Math Quiz created successfully.")

@login_required
@staff_member_required
def run_create_class12_science_quiz(request):
    from quizzes.scripts.create_class12_science_quiz import create_class12_science_quiz
    create_class12_science_quiz()
    return HttpResponse("Class 12 Science Quiz created successfully.")

@login_required
@staff_member_required
def run_create_class12_english_quiz(request):
    from quizzes.scripts.create_class12_english_quiz import create_class12_english_quiz
    create_class12_english_quiz()
    return HttpResponse("Class 12 English Quiz created successfully.")
