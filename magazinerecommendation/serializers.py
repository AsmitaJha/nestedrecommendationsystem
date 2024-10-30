from rest_framework import serializers
from .models import Magazine

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Magazine
        fields=['id','title','category']