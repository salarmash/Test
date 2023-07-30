from rest_framework import serializers
from .models import Product


class CatSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.title


class ProductSerializer(serializers.ModelSerializer):
    publisher = serializers.ReadOnlyField(source="publisher.username")
    category = CatSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
