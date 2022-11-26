from rest_framework import serializers

from acoffe.models import coffe


# class CoffeSerializer(serializers.ModelSerializer):
#     class Mets:
#         model = coffe
#         fields = ['name', 'price', 'recipe', 'exists']

class CoffeSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffe
        fields = '__all__'