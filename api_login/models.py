# -*- coding: utf-8 -*-
"""
Created on 11/10/21
@author: b4rt
@mail: root.jmn@gmail.com
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField('person_name', max_length=50, null=True)
    last_name = models.CharField('person_last_name', max_length=50, null=True)
    mail = models.CharField('mail', max_length=50, null=True)
    phone = models.IntegerField('phone', null=True)
    user = models.OneToOneField(User, to_field='id', null=True, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return '{0},{1},{2}'.format(self.mail, self.name, self.person_id)


class ProfileUser(models.Model):
    user_id = models.IntegerField('user_id', null=True)
    profile_id = models.IntegerField('profile_id', null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)


class Profiles(models.Model):
    profile_id = models.AutoField('profile_id', primary_key=True)
    profile_name = models.CharField('profile_name', max_length=50, null=True)
    status = models.BooleanField(default=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
