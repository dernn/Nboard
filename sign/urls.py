from django.urls import path

from sign.views import ConfirmUser

urlpatterns = [
    path('confirm/', ConfirmUser.as_view(), name='confirm_user'),
]
