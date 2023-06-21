from rest_framework import serializers
from . models import Product, Orders, Deliveries


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Orders
        fields = ['id', 'desc', 'price', 'amount', 'user']

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields =  ['amount', 'desc', 'price']
    def create(self, validated_data):
        # return Order.objects.create(**validated_data)
        user = self.context['user']
        return Orders.objects.create(**validated_data,user=user)

class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'
