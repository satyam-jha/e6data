
from rest_framework import serializers
from .models import CustomUser, Blog
from .utils import custom_password_validator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class CustomPasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        self.required = False
        self.validators.append(custom_password_validator)
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        data = make_password(data)
        return super().to_internal_value(data)

class CustomEmailField(serializers.EmailField):
    def to_internal_value(self, data):
        data = data.lower()
        return super().to_internal_value(data)


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, required=False)
    email = CustomEmailField(
        max_length=254,
        validators=[UniqueValidator(
            queryset=CustomUser.objects.all(),
            message="Email already exists",
            lookup='iexact'
        )]
    )
    password = CustomPasswordField()

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password'
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password')
        return data


class BlogSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = (
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'modified_at'
        )

    def create(self, validated_data):
        validated_data.update({
            'author': self.context['request'].user,

        })
        return super().create(validated_data)
