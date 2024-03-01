# content/serializers.py
from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title', 'body', 'summary', 'document', 'categories')
