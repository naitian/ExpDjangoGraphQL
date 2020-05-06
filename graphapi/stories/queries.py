import graphene

from .models import Author, Post
from .types import AuthorType, PostType, UserType


class AuthorQueries(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, id=graphene.ID(), username=graphene.String())
    me = graphene.Field(AuthorType)

    def resolve_authors(self, info):
        return Author.objects.all()

    def resolve_author(self, info, id=None, username=None):
        if id is not None:
            return Author.objects.get(pk=id)
        if username is not None:
            return Author.objects.get(user__username=username)
        return None

    def resolve_me(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Unauthenticated user")
        return Author.objects.get(user=user)


class PostQueries(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.ID(required=True))

    def resolve_posts(self, info, first=None, skip=None):
        qs = Post.objects.all()
        if skip is not None:
            qs = qs[skip:]
        if first is not None:
            qs = qs[:first]
        return qs

    def resolve_post(self, info, id):
        return Post.objects.get(pk=id)


class Query(AuthorQueries, PostQueries, graphene.ObjectType):
    pass
