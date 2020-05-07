import json

from django.contrib.auth.models import User
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase

from .models import Author, Post
from .schema import schema


class TestAuthorModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="harper", email="harperl@penguin.com", password="one_stone"
        )
        self.author = Author(user=user, description="A prolific author.")

    def test_str(self):
        assert str(self.author) == "harper"


class TestPostModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="harper", email="harperl@penguin.com", password="one_stone"
        )
        author = Author(user=user, description="A prolific author.")
        author.save()
        self.post = Post(section="News", headline="A Headline!", content="Atticus")
        self.post.save()
        self.post.authors.add(author.pk)

    def test_str(self):
        assert str(self.post) == "A Headline!"


class TestAuthorQueries(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setUp(self):
        user = User.objects.create_user(
            username="harper", email="harperl@penguin.com", password="one_stone"
        )
        author = Author(user=user, description="A prolific author.")
        author.save()
        post = Post(section="News", headline="A Headline!", content="Atticus")
        post.save()
        post.authors.add(author.pk)
        post.save()

        user = User.objects.create_user(
            username="stephen", email="stephenk@penguin.com", password="two_clowns"
        )
        author = Author(user=user, description="King of Horror")
        author.save()
        post = Post(section="Arts", headline="New Story", content="Charlene")
        post.save()
        post.authors.add(author.pk)
        post.save()

    def test_author_query_with_id(self):
        response = self.query(
            """
            query {
                author(id: 1) {
                    id
                    username
                    email
                }
            }
            """,
            op_name="author",
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content["data"]["author"]["id"] == "1"
        assert content["data"]["author"]["username"] == "harper"

    def test_author_query_with_username(self):
        response = self.query(
            """
            query {
                author(username: "harper") {
                    id
                    username
                    email
                }
            }
            """,
            op_name="author",
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content["data"]["author"]["id"] == "1"
        assert content["data"]["author"]["username"] == "harper"

    def test_invalid_author_queries(self):
        query = """
            query GetAuthor($id: ID, $username: String){
                author(id: $id, username: $username) {
                    id
                    username
                    email
                }
            }
        """
        response = self.query(query, op_name="GetAuthor")
        content = json.loads(response.content)
        assert "errors" in content
        assert (
            content["errors"][0]["message"]
            == "Must specify exactly one of id or username"
        )
        response = self.query(
            query, op_name="GetAuthor", variables={"id": "1", "username": "bartholomew"}
        )
        content = json.loads(response.content)
        assert "errors" in content
        assert (
            content["errors"][0]["message"]
            == "Must specify exactly one of id or username"
        )

    def test_authors_query(self):
        response = self.query(
            """
            query {
                authors {
                    id
                    username
                    posts {
                        headline
                    }
                }
            }
            """,
            op_name="author",
        )
        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
        assert content["data"] == {
            "authors": [
                {"id": "1", "username": "harper", "posts": [{"headline": "A Headline!"}]},
                {"id": "2", "username": "stephen", "posts": [{"headline": "New Story"}]},
            ],
        }
