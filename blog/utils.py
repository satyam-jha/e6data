from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import get_default_password_validators
from rest_framework.pagination import LimitOffsetPagination

def custom_password_validator(password, user=None, password_validators=None):
    errors = []
    if ' ' in password:
        errors.append('Password cannot contain blank space')
    if password_validators is None:
        password_validators = get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, user)
        except ValidationError as error:
            errors.extend(error.messages)

    if errors:
        if user:
            raise serializers.ValidationError(detail={'password': errors})
        else:
            raise serializers.ValidationError(detail=errors)


def get_jwt_auth_token(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CustomLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 100