# Nboard
Интернет-ресурс для фанатского сервера одной известной MMORPG [доска объявлений].

* Bootstrap
* Django
* login/register on django-allauth
  * OAuth2 on Google Ads API
* Mailing on Celery scheduler [+ Redis server]
* CKEditor WYSIWYG
* Flake8 Style Guide

---

### Техническое задание

Пользователи ресурса имеют возможность зарегистрироваться по e-mail, получив на почту письмо с кодом подтверждения регистрации. Также есть возможность авторизации через Google OAuth.

После регистрации пользователям становится доступно создание и редактирование объявлений.

Объявления состоят из заголовка и текста, внутри которого могут быть картинки, встроенные видео и другой контент.

Пользователи могут отправлять отклики на объявления других пользователей, состоящие из простого текста.

При отправке отклика пользователь (автор объявления) получает e-mail с оповещением о нём.

Пользователю (автору объявления) доступна приватная страница с откликами на его объявления, внутри которой он может фильтровать отклики по объявлениям, удалять их и принимать (при принятии отклика пользователю, оставившему отклик, также приходит уведомление).

Кроме того, пользователь обязательно должен определить объявление в одну из следующих категорий: Танки, Хилы, ДД, Торговцы, Гилдмастеры, Квестгиверы, Кузнецы, Кожевники, Зельевары, Мастера заклинаний.

Также есть возможность отправлять пользователям новостные рассылки.

---

КЛЮЧЕВЫЕ ОСОБЕННОСТИ:

- Категории импортируются в базу данных из [BASE_DIR / 'fixtures'];
- Добавление объявлений/откликов доступно только авторизованным пользователям;
- Редактирование объявления доступно только автору объявления;
- Текст объявления представляет собой поле `RichTextUploadingField` *[ckeditor]*, внутри которого могут быть *[загружаемые]* картинки, встроенные видео *[youtube plugin]* и кастомный текст;
- Пользователю (автору объявления) доступна приватная страница с откликами на его объявления [dropdown -> Personal page], внутри которой он может:
  - фильтровать отклики по объявлениям;
  - удалять их;
  - принимать или отклонять.

---

***Письма отправляются по следующим событиям:***
```
- регистрироваться по e-mail: письмо с кодом подтверждения на почту;
- пользователь оставил отклик к объявлению [автор получает письмо];
- пользователь (автор объявления) удалил/принял/отклонил отклик
  [автор отклика получает письмо; на каждый случай уникальный шаблон];
- новостная рассылка каждый понедельник в 8.00 утра по UTC
  (все объявления за последнюю неделю всем пользователям).
```
*[отправка писем реализована через celery + локальный redis server].*

#
*для запуска celery воркера/периодических задач [в разных окнах терминала]:*
```
celery -A <project_name> worker -l INFO --pool=solo
celery -A <project_name> beat -l INFO
```
**перед этим запустив **redis-server.exe***
