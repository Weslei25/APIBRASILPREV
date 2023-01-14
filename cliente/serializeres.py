from rest_framework import serializers
from django.contrib.auth.models import User, Group
from cliente.models import ClienteModel


class ClienteSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return super().create(**validated_data)

    class Meta:
        model = ClienteModel
        fields = '__all__'

        