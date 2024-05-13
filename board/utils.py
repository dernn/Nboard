from django.shortcuts import render

from board.models import Post


def comment_in_user_post(request, comment):
    """
    Метод проверяет, входит ли пост, к которому принадлежит переданный комментарий,
    во множество всех постов, принадлежащих автору.
    Если нет - рендерит страницу блокировки.
    """
    comment_post = comment.post
    user_posts = Post.objects.filter(author=request.user)
    if comment_post not in user_posts:
        context = {'comment_id': comment.id}
        return render(request, template_name='board/comment_lock.html', context=context)

    else:
        return True
