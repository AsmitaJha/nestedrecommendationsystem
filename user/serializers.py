from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "favorite_genres",
            "favorite_music_genres",
            "favorite_magazine_categories",
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        favorite_genres = validated_data.pop("favorite_genres", [])
        favorite_music_genres = validated_data.pop("favorite_music_genres", [])
        favorite_magazine_categories = validated_data.pop(
            "favorite_magazine_categories", []
        )

        # creating user instance and hashing password
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])  # Hashes the password
        user.save()  # Saving the user before adding many to many fields

        # Adding many to many fields
        user.favorite_genres.set(favorite_genres)
        user.favorite_music_genres.set(favorite_music_genres)
        user.favorite_magazine_categories.set(favorite_magazine_categories)

        return user
