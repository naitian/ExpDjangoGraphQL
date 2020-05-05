from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    section = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="posts"
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    headline = models.CharField(max_length=128)
    content = models.TextField()

    def __str__(self):
        return str(self.headline)
