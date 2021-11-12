# -*- coding: utf-8 -*-
"""
Created on 11/11/21
@author: b4rt
@mail: root.jmn@gmail.com
"""

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api_dog_manager.models import Walker, WalkerxDog


class WalkerSerializer:
    class Meta:
        model = Walker
        fields = '__all__'

    walker_id = serializers.IntegerField(required=True, allow_null=False)
    user = serializers.IntegerField(required=True, allow_null=False)

    def create(self, validated_data):
        return Walker.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.walker_id = validated_data.get('walker_id', instance.walker_id)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


class WalkerxDogSerializer:
    class Meta:
        model = WalkerxDog
        fields = '__all__'

    walker = serializers.IntegerField(required=True, allow_null=False)
    dog = serializers.IntegerField(required=True, allow_null=False)

    def create(self, validated_data):
        return WalkerxDog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.walker = validated_data.get('walker', instance.walker)
        instance.dog = validated_data.get('dog', instance.dog)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


c
