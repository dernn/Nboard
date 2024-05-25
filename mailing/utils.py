import datetime

from django.conf import settings  # LazySettings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from board.models import Post, Category


def send_notification(text, pk, category, title, subscriber, sender, mode='create'):
    """
    Метод формирует контекст для почтового шаблона, на основе полученных
    из таски параметров создаёт письмо, прикрепляет к нему
    контент [шаблон + контекст] и отправляет адресату.

    :param text: текст комментария
    :param pk: id связанного* поста
    :param category: категория поста*
    :param title: заголовок поста*
    :param subscriber: автор поста*
    :param sender: автор комментария
    :param mode: задаёт шаблон и тему письма
    """

    if mode == 'create':
        template = 'comment_created_email'
        subject = f'Reply to "{title}"'
    elif mode == 'update':
        template = 'comment_updated_email'
        # can be fixed through param 'accepted' [передавать объект целиком?]
        subject = f'{sender} has accepted/declined your response'

    html_content = render_to_string(
        # template changes depending on the mode
        f'mailing/{template}.html',
        {
            'text': text,
            'link': f'{settings.SITE_URL}/board/{pk}',
            'username': subscriber.username,
            'category': category,
            'sender': sender,
        }
    )

    msg = EmailMultiAlternatives(
        # subject changes depending on the mode
        subject=subject,
        body='',  # body задаем выше в html_content
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[subscriber.email],
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


# def weekly_mailing():
#     #  Your job processing logic here...
#     today = datetime.datetime.now()
#     last_week = today - datetime.timedelta(days=7)
#     posts = Post.objects.filter(pub_date__gte=last_week)  # lookup __gte
#     categories = set(posts.values_list('category__name', flat=True))
#     categories.remove(None)
#     subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
#
#     html_content = render_to_string(
#         'mailing/weekly_news.html',
#         {
#             'link': settings.SITE_URL,
#             'posts': posts,
#         }
#     )
#
#     # время отправки без микросекунд для заголовка
#     sending_time = datetime.datetime.now().replace(microsecond=0)
#
#     msg = EmailMultiAlternatives(
#         subject=f'News from last week {sending_time}',  # тема письма
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#     print(f'msg sent {sending_time}')
