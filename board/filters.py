from django_filters import FilterSet, ModelChoiceFilter, CharFilter
from django.forms import Select
from board.models import Post


def posts(request):
    if request is None:
        return Post.objects.none()

    user = request.user
    return user.post_set.all()


class PostFilter(FilterSet):
    title = ModelChoiceFilter(queryset=posts)

    # class Meta:
    #     model = Post
    #     fields = ['title', ]
    # class Meta:
    #     model = Post
    #     fields = {
    #         'title': ['icontains'],
    #     }
