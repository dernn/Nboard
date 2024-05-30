from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import html


# define AUTH_USER_MODEL in settings
class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=60, default='Title')
    text = RichTextUploadingField()

    def __str__(self):
        return f'{self.title}'

    def preview(self):
        result = html.strip_tags(self.text)
        return f'{result[:40]}...'

    def get_absolute_url(self):
        return f'/board/{self.id}'


class Comment(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    accept = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/board/{self.post.id}'
