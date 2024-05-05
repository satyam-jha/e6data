from django.db import transaction
from blog.models import CustomUser, Blog
from blog.utils import get_jwt_auth_token
from blog.filters import BlogFilter
from blog.serializer import CustomUserSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, \
    RetrieveModelMixin


def success_response(data=None, message=None, request=None, extra_data={}):
    result = {'status': {'code': status.HTTP_200_OK,
                         'message': message},
              'data': data
              }
    result.update(extra_data)
    return Response(result)


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = 'on_boarding'

    @transaction.atomic
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data, context={'request': request, 'view': self})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return success_response(data=serializer.data, extra_data={'token': get_jwt_auth_token(user)})


class BlogBaseApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().select_related('author')
    filter_class = BlogFilter

    def initial(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.permission_classes = (AllowAny,)

        super().initial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BlogDetailApiView(BlogBaseApiView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
