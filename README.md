# GraphQL API with Django

## Quickstart

To get set up:

```
# create a virtual environment
python3 -m venv env
source env/bin/activate
# install dependencies
pip install -r requirements.txt
./manage.py migrate  # make database migrations
./manage.py createsuperuser  # set up admin acct
./manage.py runserver  # run server locally
```

To view the admin interface, navigate to `localhost:8000/admin/`.

To view the GraphiQL interface, navigate to `localhost:8000/graphql/`.

To interface with the database through a Python REPL, run `./manage.py shell`

## Parts:

- [Django](https://docs.djangoproject.com/en/3.0/) (obviously).
- [Graphene](https://graphene-python.org/) and [Graphene Django](https://docs.graphene-python.org/projects/django/en/latest/) for GraphQL
- [`django-cors-headers`]() for enabling CORS
- [`django-graphql-jwt`](https://django-graphql-jwt.domake.io/en/latest/authentication.html) for authentication with JSON Web Tokens
