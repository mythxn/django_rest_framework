from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all(),
    )


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ["id", "owner", "title", "code", "lineos", "language", "style"]
