# -*- coding: utf-8 -*-
"""
Created on 11/11/21
@author: b4rt
@mail: root.jmn@gmail.com
"""
from gettext import gettext, pgettext

from django.http.response import JsonResponse
from django.utils.functional import lazy
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken

from api_login.serializers import UserSerializer
from django.utils.translation import gettext as _

from project_dogger.services import custom_response


class LoginSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': custom_response.response_error(message="Usuario o contraseña incorrecta",
                                                            type_response=False)
    }

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token': _('Token is invalid or expired')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
