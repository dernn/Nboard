from board.views import PostListView

from django.urls import path

urlpatterns = [
    path('board/', PostListView.as_view()),
]
