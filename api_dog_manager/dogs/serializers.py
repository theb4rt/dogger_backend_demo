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
from api_dog_manager.models import Dogs, Walker, WalkerxDog


class DogsSerializer(serializers.Serializer):
    class Meta:
        model = Dogs
        fields = '__all__'

    dog_size = serializers.CharField(required=True, allow_blank=False, max_length=100)
    dog_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    dog_age = serializers.IntegerField(required=False, allow_blank=True, allow_null=True, default=None)
    person = serializers.IntegerField(required=True, allow_null=False)

    def create(self, validated_data):
        return Dogs.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dog_size = validated_data.get('dog_size', instance.dog_size)
        instance.dog_name = validated_data.get('dog_name', instance.dog_name)
        instance.dog_age = validated_data.get('dog_age', instance.dog_age)
        instance.person = validated_data.get('person', instance.person)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


