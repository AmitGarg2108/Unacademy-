from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, UserQuizScore
from .forms import ProfileForm

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    previous_scores = UserQuizScore.objects.filter(user=request.user).order_by('-date_taken')
    return render(request, 'profiles/profile.html', {'profile': profile, 'previous_scores': previous_scores})

@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})
