from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.forms import ReviewForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@login_required
def about(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('accounts:about')
    else:
        form = ReviewForm()
    return render(request, 'about.html', {'form': form})
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    # Pass CSRF token explicitly for JS usage
    from django.middleware.csrf import get_token
    from profiles.models import Profile
    csrf_token = get_token(request)
    # Static latest news data
    latest_news = [
        {'title': 'CBSE announces new exam pattern for Class 10', 'url': 'https://cbse.nic.in/new-exam-pattern-class10'},
        {'title': 'NTA releases JEE Main 2025 schedule', 'url': 'https://nta.ac.in/jeemain2025-schedule'},
        {'title': 'ICSE updates syllabus for Science subject', 'url': 'https://cisce.org/science-syllabus-update'},
        {'title': 'UP Board results declared for 12th class', 'url': 'https://upmsp.edu.in/12th-results'},
        {'title': 'NTA invites applications for UGC NET June 2025', 'url': 'https://nta.ac.in/ugcnet-june-2025'},
    ]
    username = None
    profile_picture_url = None
    if request.user.is_authenticated:
        username = request.user.username
        try:
            profile = Profile.objects.get(user=request.user)
            if profile.profile_picture:
                profile_picture_url = profile.profile_picture.url
        except Profile.DoesNotExist:
            profile_picture_url = None
    return render(request, 'accounts/home.html', {'csrf_token': csrf_token, 'latest_news': latest_news, 'username': username, 'profile_picture_url': profile_picture_url})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Provide backend explicitly due to multiple authentication backends
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserCreationForm()
    # Clear form data on GET to prevent previous user info showing
    form.data = form.data.copy()
    form.data.clear()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')
    else:
        form = AuthenticationForm()
    # Clear form data on GET to prevent previous user info showing
    form.data = form.data.copy()
    form.data.clear()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile_view(request):
    from profiles.models import Profile, UserQuizScore
    profile, created = Profile.objects.get_or_create(user=request.user)
    previous_scores = UserQuizScore.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'profiles/profile.html', {'profile': profile, 'previous_scores': previous_scores})

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def ai_chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        # Dummy AI response for demonstration
        ai_response = f"AI says: You said '{user_message}'. This is a demo response."
        return JsonResponse({'response': ai_response})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
