from rest_framework import serializers
from .models import fish

class fishSerializer(serializers.ModelSerializer):

    class Meta:
        model = fish
        fields = '__all__'