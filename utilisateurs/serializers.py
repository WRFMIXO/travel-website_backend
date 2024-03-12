from rest_framework import serializers
from .models import CustomUser


# Sérialiseur pour la création d'un utilisateur
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

# Sérialiseur pour la mise à jour d'un utilisateur
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Serialiseur pour le listing des utilisateurs
class ListUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
