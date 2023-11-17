from django.shortcuts import render
from rest_framework import viewsets
from .models import Posting
from .serializer import PostSerializer
# Create your views here.

class Postview(viewsets.ModelViewSet):
    queryset=Posting.objects.all()
    serializer_class=PostSerializer
