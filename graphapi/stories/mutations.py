import graphene
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphql_jwt.decorators import login_required

from .forms import AuthorForm, PostForm
from .models import Author, Post
from .types import AuthorType, PostType, UserType


class PostMutation(DjangoModelFormMutation):
    post = graphene.Field(PostType)

    class Meta:
        form_class = PostForm


class AuthorMutation(DjangoModelFormMutation):
    author = graphene.Field(AuthorType)

    class Meta:
        form_class = AuthorForm

    @classmethod
    @login_required
    def perform_mutate(form, info):
        super(form, info)


class Mutation(graphene.ObjectType):
    update_post = PostMutation.Field()
    update_author = AuthorMutation.Field()
