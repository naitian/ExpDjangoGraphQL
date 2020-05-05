import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Author, Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = (
            "section",
            "author",
            "updated",
            "created",
            "headline",
            "content",
            "id",
        )


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("description", "posts", "id")

    username = graphene.String()
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

    def resolve_username(self, info):
        if self is not None:
            return self.user.username
        return None

    def resolve_email(self, info):
        if self is not None:
            return self.user.email
        return None

    def resolve_first_name(self, info):
        if self is not None:
            return self.user.first_name
        return None

    def resolve_last_name(self, info):
        if self is not None:
            return self.user.last_name
        return None


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
