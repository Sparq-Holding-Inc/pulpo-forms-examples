
from rest_framework import serializers
from pulpo_example.models import PulpoUser, Club, Country


class PulpoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = PulpoUser
        fields = ('name', 'last_name', 'birthdate', 'has_car')


class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ('name', 'established', 'country')


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('name',)
