from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'image', 'excerpt', 'content', 'status']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']