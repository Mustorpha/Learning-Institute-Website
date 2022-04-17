from .models import Comment, Subscription, Application
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('title', 'full_name', 'gender', 'address', 'date_of_birth', 'email', 'course', 'photograph', 'form')