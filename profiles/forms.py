from django import forms
from .models import Review, Profile

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
        labels = {
            'content': 'Review',
            'rating': 'Rating (1-5)',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['class_name', 'entrance_exam', 'profile_picture']
        widgets = {
            'class_name': forms.TextInput(attrs={'placeholder': 'Enter your class'}),
            'entrance_exam': forms.TextInput(attrs={'placeholder': 'Enter your entrance exam'}),
        }
