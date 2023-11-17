from rest_framework import serializers
from .models import Posting

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ('url','title', 'content')