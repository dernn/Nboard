from django.shortcuts import render

from board.models import Post


def comment_not_in_user_post(request, comment):
    """
    Метод проверяет, входит ли пост, к которому принадлежит переданный комментарий,
    во множество всех постов, принадлежащих автору.
    """
    comment_post = comment.post
    user_posts = Post.objects.filter(author=request.user)
    return comment_post not in user_posts
