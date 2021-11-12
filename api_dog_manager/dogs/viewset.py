# -*- coding: utf-8 -*-
"""
Created on 11/11/21
@author: b4rt
@mail: root.jmn@gmail.com
"""

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from api_dog_manager.dogs.serializers import DogsSerializer
import project_dogger.services.custom_response as custom_response


class DogViewSet(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request, format=None):
        serializer = DogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
