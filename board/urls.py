from board.views import PostListView, PostDetailView, CategoryListView, PostCreateView

from django.urls import path

urlpatterns = [
    path('board/', PostListView.as_view()),
    path('board/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>', CategoryListView.as_view(), name='post_category'),
    path('add/', PostCreateView.as_view(), name='post_create'),
]
