from rest_framework import serializers
from blog import models


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Blog
