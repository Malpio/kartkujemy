from django.db import models
from users.models import User
import uuid


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    title = models.CharField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='media/')
    author_name = models.CharField(max_length=200)
    general_rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)


class BooksOfUsers(models.Model):
    class Types(models.TextChoices):
        NO_CHOOSE = "Nie wybrano",
        TO_READ = "Do przeczytania",
        READ = "Przeczytana",
        ABANDONED = "Porzucona",

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Types.choices, default=Types.NO_CHOOSE)
    rating = models.IntegerField(default=0)
    opinion = models.CharField(max_length=300)

