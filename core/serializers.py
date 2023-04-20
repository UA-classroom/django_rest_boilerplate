from rest_framework import serializers
from .models import Product, Order, OrderItem, Review

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'available', 'reviews',)

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        product = Product.objects.create(**validated_data)
        if reviews_data:
            for review_data in reviews_data:
                Review.objects.create(product=product, **review_data)
        return product
    
    # This is the update method, it tends to get complicated because it has to handle multiple cases.
    # E.g - What if the list is empty, meaning there are no reviews?
    # Or if the list is not empty, then we have to create new ones or update existing ones.
    def update(self, instance, validated_data):
        reviews_data = validated_data.pop('reviews', None)
        # Update the product regardless of whether there are reviews or not using .super()
        instance = super().update(instance, validated_data)
        # The rest is custom logic for our specific use case / serializer
        if reviews_data:
            for review_data in reviews_data:
                _, created = Review.objects.update_or_create(
                    id=review_data.get('id', None),
                    defaults={
                        'product': instance,
                        'text': review_data.get('text', None),
                        'rating': review_data.get('rating', None),
                        'user': review_data.get('user', None)
                    }
                )
        return instance

class OrderItemModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer()
    
    class Meta:
        model = OrderItem
        fields = '__all__'

    # Add a update and create method

class OrderModelSerializer(serializers.ModelSerializer):
    # We can't add an order with order items unless we override the create method
    # or override the update method 

    # Before we added this we only saw a list of order item id's, e.g [1,2], with this
    # we get the dictionaries
    order_items = OrderItemModelSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = '__all__'


# Some data to test adding a review

# {
#     "name": "Product 1",
#     "description": "This is a sample product.",
#     "price": "19.99",
#     "available": true,
#     "reviews": [
#         {
#             "text": "This product is amazing!",
#             "rating": 5,
#             "user": 1,
#             "product": 1
#         },
#         {
#             "text": "I didn't like this product!!!!!!!!!!!!!!!ASDSADS!!!!!!.",
#             "rating": 2,
#             "user": 1,
#             "product": 1
#         }
#     ]
# }
