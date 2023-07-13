from django.contrib.auth import get_user_model


from rest_framework import serializers
from .models import Product

User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    upper_title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'content', 'sale_price', 'my_discount', 'upper_title']

    def get_my_discount(self, obj):
        return obj.get_discount()

    def get_upper_title(self, obj):
        return obj.get_upper_title()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'id',
            'email',
            'password'
        ]
