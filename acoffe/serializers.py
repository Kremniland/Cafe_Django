from rest_framework import serializers

from acoffe.models import coffe, ingridient


class CoffeSerializer(serializers.ModelSerializer):
    class Meta:
        model = coffe
        fields = ['pk', 'name', 'description', 'price', 'exists',]

class IngridientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ingridient
        fields = ['pk', 'name', 'description', 'price', 'exists', 'coffe']
        