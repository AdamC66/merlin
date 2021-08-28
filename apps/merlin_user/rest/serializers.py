from apps.merlin_user.models import MerlinUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerlinUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "code",
            "company",
            "avatar",
        ]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MerlinUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "code",
            "company",
            "avatar",
            "address_line_1",
            "address_line_2",
            "address_city",
            "address_state",
            "address_zip",
            "address_country",
            "address_phone",
        ]