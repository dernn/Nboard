from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from mailing.tasks import celery_notify_create_comment, celery_notify_update_comment, celery_notify_delete_comment
from board.models import Comment


@receiver(post_save, sender=Comment)  # Comment --> Post (1)
def notify_about_save_comment(sender, instance, **kwargs):  # instance : объект статьи
    """
    Сигнал срабатывает при создании/редактировании комментария к посту
    и вызывает соответсвующую таску из mailing.tasks;
    метод 'delay' передает не объект, но только id экземпляра.

    :param instance: экземпляр модели Comment
    """
    # Comment --> Post
    if kwargs['created']:  # kwargs['created'] == True
        celery_notify_create_comment.delay(instance.pk)
    # Accept/Decline --> Comment
    elif kwargs['update_fields']:
        celery_notify_update_comment.delay(instance.pk)


# Delete --> Comment
@receiver(pre_delete, sender=Comment)
def notify_about_delete_comment(sender, instance, **kwargs):
    """
    Сигнал срабатывает вначале удаление экземпляра модели Comment;
    в вызываемую таску передается полностью удаляемый объект.
    """
    celery_notify_delete_comment(instance.pk)

