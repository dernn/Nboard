from board.views import PostListView, PostDetailView, CategoryListView, PostCreateView, PostUpdateView, \
    CommentCreateView, PersonalSearchListView

from django.urls import path

urlpatterns = [
    path('board/', PostListView.as_view()),
    path('board/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>', CategoryListView.as_view(), name='post_category'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('board/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('board/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('board/personal/', PersonalSearchListView.as_view(), name='personal_search'),
]
