from django.db.models.signals import post_save
from django.dispatch import receiver

from mailing.tasks import celery_notify_new_comment
from board.models import Post, Comment


@receiver(post_save, sender=Comment)  # Comment --> Post (1)
def notify_about_new_comment(sender, instance, **kwargs):  # instance : объект статьи
    """
    Сигнал срабатывает при создании нового комментария к посту
    и вызывает таску 'celery_notify_new_comment' из mailing.tasks;
    методом 'delay' передает не объект, но только id экземпляра

    :param instance: экземпляр модели Comment
    """
    if kwargs['created']:  # kwargs['created'] == True
        celery_notify_new_comment.delay(instance.pk)

# Accept[/Delete/Decline] --> Comment (2[/3/4])
