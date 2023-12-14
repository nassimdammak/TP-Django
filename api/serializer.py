from rest_framework import serializers
from .models import Concessionnaire, Voiture

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        exclude = ['numero_siret']  

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'  
