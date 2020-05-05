import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from .mutations import Mutation
from .queries import Query


schema = graphene.Schema(query=Query, mutation=Mutation)
