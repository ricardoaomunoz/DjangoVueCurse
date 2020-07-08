# aplicacion que sea consumida desde una rest api, solo brinda los datos con los cuales vamos a trabajar (json, definir el formato y hacer validaciones previas)

from rest_framework import serializers

from .models import Element, Category, Type

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'

class ElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Element
        fields = '__all__'