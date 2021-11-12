# -*- coding: utf-8 -*-
"""
Created on 11/10/21
@author: b4rt
@mail: root.jmn@gmail.com
"""
from django.db import transaction
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.validators import UniqueValidator

from api_login.models import Person, User, ProfileUser

UserModel = get_user_model()


class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ("username", "password", "email", "first_name", "last_name", "phone")

    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Usuario ya existe")], required=True,
        allow_blank=False, max_length=50)
    password = serializers.CharField(required=True, allow_blank=False, write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="Email ya existe")],
                                   required=True,
                                   allow_blank=False, max_length=50)
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=50, )
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=50, default=None)
    phone = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=2, default=None)

    @transaction.atomic
    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    @transaction.atomic
    def create_user_custom(self, user_data):
        final_user_data = {
            'username': user_data.get("username", None),
            'password': user_data.get("password", None),
            'first_name': user_data.get("name", None),
            'last_name': user_data.get("last_name", None),
            'email': user_data.get("email", None),
        }
        user = self.create(validated_data=final_user_data)

        user_id = user.id
        person_data = {
            'name': user_data.get("first_name", None),
            'last_name': user_data.get("last_name", None),
            'phone': user_data.get("phone", None),
            'mail': user_data.get("email", None),
            'user_id': user_id
        }
        person = PersonSerializer().create(validated_data=person_data)
        profile_data = {
            'user_id': user_id,
            'profile_id': user_data.get("profile_id", 1),
        }
        profile = ProfileUserSerializer().create(validated_data=profile_data)
        return person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_blank=False, max_length=50, )
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True, max_length=50, default=None)
    phone = serializers.CharField(required=False, allow_blank=True, allow_null=True, default=None)
    mail = serializers.EmailField(required=True, allow_blank=False, max_length=50)
    user_id = serializers.IntegerField(required=True)

    @transaction.atomic
    def create(self, validated_data):
        person = Person.objects.create(**validated_data)

        return person

    class Meta:
        model = Person
        fields = ("mail", "name", "last_name")


class ProfileUserSerializer(serializers.Serializer):
    @transaction.atomic()
    def create(self, validated_data):
        return ProfileUser.objects.create(**validated_data)
