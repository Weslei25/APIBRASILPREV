from rest_framework import serializers
from django.contrib.auth.models import User, Group
from plano.models import PlanoModel, AporteExtraModel, ResgateModel


class PlanoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanoModel
        fields = '__all__'

        
class AporteExtraSerializer(serializers.ModelSerializer):

    class Meta:
        model = AporteExtraModel
        fields = '__all__'

class ResgateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResgateModel
        fields = '__all__'
