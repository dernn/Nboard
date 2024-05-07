from board.forms import CommentForm, PostForm
from board.models import Comment, Post

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class PostListView(ListView):
    model = Post
    ordering = '-pub_date'
    template_name = 'board/index.html'
    context_object_name = 'postlist'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    permission_required = ('board.add_post',)
    template_name = 'board/post_create.html'

    # Field.initial/Field.disabled alt. solution
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('board.change_post',)
    template_name = 'board/post_edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    # author verification
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()

        context = {'post_id': post.pk}
        if post.author != self.request.user:
            return render(self.request, template_name='board/post_lock.html', context=context)

        return super(PostUpdateView, self).dispatch(request, *args, **kwargs)


# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'board/post_delete.html'
#     success_url = '/board/'
#
#     # author verification
#     def dispatch(self, request, *args, **kwargs):
#         post = self.get_object()
#
#         context = {'post_id': post.pk}
#         if post.author != self.request.user:
#             return render(self.request, template_name='board/post_lock.html', context=context)
#
#         return super(PostDeleteView, self).dispatch(request, *args, **kwargs)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'board/comment_create.html'
    context_object_name = 'comment'


class CommentDetailView(DetailView):
    pass


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    pass


# ~для PrivateSearchListView
class CommentDeleteView(DeleteView):
    pass


# приватная страница с откликами на объявления пользователя,
# внутри которой он может фильтровать отклики по объявлениям,
# удалять их и принимать (~перенести в sign/protect)
class PrivateSearchListView(LoginRequiredMixin, ListView):
    model = Comment
    pass
