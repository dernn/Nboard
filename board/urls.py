from board.views import PostListView, PostDetailView, CategoryListView, PostCreateView, PostUpdateView, \
    CommentCreateView, PersonalSearchListView

from django.urls import path

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>', CategoryListView.as_view(), name='post_category'),
    path('post/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('personal/', PersonalSearchListView.as_view(), name='personal_search'),
]
