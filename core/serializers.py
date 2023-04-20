from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderModelSerializer(serializers.ModelSerializer):
    # We can't add an order with order items unless we override the create method
    # or override the update method 

    # Before we added this we only saw a list of order item id's, e.g [1,2], with this
    # we get the dictionaries
    order_items = OrderItemModelSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = '__all__'

