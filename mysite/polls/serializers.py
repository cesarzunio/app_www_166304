from rest_framework import serializers
from .models import Team, Person, Stanowisko, Osoba
from datetime import datetime


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'surname', 'shirt_size', 'month_added', 'team']


class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']


class OsobaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Osoba's name must consist only of letters!")

        return value

    def validate_data_dodania(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("Osoba's creation date cannot be date from the future!")

        return value
