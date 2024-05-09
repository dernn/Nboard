from board.forms import CommentForm, PostForm
from board.models import Comment, Post, Category

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
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


class PostCreateView(CreateView):
    template_name = 'board/post_create.html'
    form_class = PostForm

    # Field.initial/Field.disabled alt. solution
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
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


class CategoryListView(PostListView):
    template_name = 'board/post_category.html'
    context_object_name = 'post_category'

    def get_queryset(self):
        # current category instance
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'board/comment_create.html'
    context_object_name = 'comment'


class CommentDetailView(DetailView):
    pass


class CommentUpdateView(UpdateView):
    pass


# ~для PrivateSearchListView
class CommentDeleteView(DeleteView):
    pass


# приватная страница с откликами на объявления пользователя,
# внутри которой он может фильтровать отклики по объявлениям,
# удалять их и принимать (~перенести в sign/protect)
class PrivateSearchListView(ListView):
    model = Comment
    pass
