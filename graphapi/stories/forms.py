from django.forms import ModelForm

from .models import Author, Post


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['user', 'description']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['section', 'authors', 'headline', 'content']
