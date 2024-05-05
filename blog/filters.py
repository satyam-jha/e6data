from django_filters import rest_framework as filters
from blog.models import Blog


class BlogFilter(filters.FilterSet):

    class Meta:
        model = Blog
        fields = ('author',)
