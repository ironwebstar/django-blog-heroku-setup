from rest_framework import generics

from blog import models
from . import serializers

# Create your views here.


class BlogList(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class BlogDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

