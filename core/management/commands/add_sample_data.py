from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Product, Order, OrderItem

class Command(BaseCommand):
    help = 'Adds sample data for Products, Users, and Orders.'

    def handle(self, *args, **options):
        # Create sample products
        products = [
            Product(name="Product 1", description="Sample product 1", price="9.99"),
            Product(name="Product 2", description="Sample product 2", price="19.99"),
            Product(name="Product 3", description="Sample product 3", price="29.99"),
        ]

        for product in products:
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.name}'))

        # Create a sample user
        user = User(username="testuser", email="testuser@example.com")
        user.set_password("testpassword")
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created user: testuser'))

        # Create sample orders
        orders = [
            Order(user=user, total_price="39.98"),
            Order(user=user, total_price="29.99"),
        ]

        for order in orders:
            order.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created order: {order.id}'))

        # Create sample order items
        order_items = [
            OrderItem(order=orders[0], product=products[0], quantity=2),
            OrderItem(order=orders[0], product=products[1], quantity=1),
            OrderItem(order=orders[1], product=products[2], quantity=1),
        ]

        for order_item in order_items:
            order_item.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created order item: {order_item.id}'))