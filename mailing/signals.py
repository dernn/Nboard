from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from mailing.tasks import celery_notify_create_comment, celery_notify_update_comment
from board.models import Post, Comment


@receiver(post_save, sender=Comment)  # Comment --> Post (1)
def notify_about_create_comment(sender, instance, **kwargs):  # instance : объект статьи
    """
    Сигнал срабатывает при создании/редактировании комментария к посту
    и вызывает соответсвующую таску из mailing.tasks;
    методом 'delay' передает не объект, но только id экземпляра

    :param instance: экземпляр модели Comment
    """
    # Comment --> Post
    if kwargs['created']:  # kwargs['created'] == True
        celery_notify_create_comment.delay(instance.pk)
    # Accept/Decline --> Comment
    elif kwargs['update_fields']:
        celery_notify_update_comment.delay(instance.pk)


# Delete --> Comment (2)
# @receiver(post_delete, sender=Comment)  # Comment --> Post (1)
# def notify_about_new_comment(sender, instance, **kwargs):  # instance : объект статьи
#     if kwargs['created']:  # kwargs['created'] == True
#         celery_notify_new_comment.delay(instance.pk)

