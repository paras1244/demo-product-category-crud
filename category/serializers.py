
from .models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "parent",
            "created_at",
            "updated_at",
            "is_parent"
        ]
