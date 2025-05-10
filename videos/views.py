from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import VideoLecture

@login_required
def video_lectures_view(request):
    class_name = request.GET.get('class_name', '')
    entrance_exam = request.GET.get('entrance_exam', '')

    videos = VideoLecture.objects.all()
    if class_name:
        videos = videos.filter(class_name=class_name)
    if entrance_exam:
        videos = videos.filter(entrance_exam=entrance_exam)

    return render(request, 'videos/video_lectures.html', {'videos': videos})

@login_required
def video_lecture_detail_view(request, pk):
    video = get_object_or_404(VideoLecture, pk=pk)
    return render(request, 'videos/video_lecture_detail.html', {'video': video})
