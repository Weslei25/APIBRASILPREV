from rest_framework import serializers
from django.contrib.auth.models import User, Group
from produto.models import ProdutoModel


class ProdutoSerializer(serializers.ModelSerializer):

    """    def create(self, validated_data):
            return super().create(**validated_data)"""

    class Meta:
        model = ProdutoModel
        fields = '__all__'

        