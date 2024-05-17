from celery import shared_task

from mailing.utils import send_notification
# from mailing.utils import weekly_mailing
from board.models import Post, Comment


@shared_task
def celery_notify_new_comment(pk):
    """
    Таска вызывает метод 'send_notification' и передает в него ряд параметров
    для формирования и отправки почтового уведомления.
    """
    instance = Comment.objects.get(pk=pk)
    post = instance.post
    subscriber = post.author
    sender = instance.author

    send_notification(instance.text, post.pk, post.category, post.title, subscriber, sender)


# @shared_task
# def celery_weekly_mailing():
#     # функцию еженедельной рассылки импортируем из утилит,
#     weekly_mailing()
