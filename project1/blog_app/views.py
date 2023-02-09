from django.shortcuts import render
from . serializers import BlogSerializer
from .models import Blog
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
