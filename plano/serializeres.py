from rest_framework import serializers
from django.contrib.auth.models import User, Group
from plano.models import PlanoModel


class PlanoSerializer(serializers.ModelSerializer):

    """    def create(self, validated_data):
            return super().create(**validated_data)"""

    class Meta:
        model = PlanoModel
        fields = '__all__'

        