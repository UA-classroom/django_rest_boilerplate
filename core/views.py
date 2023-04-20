from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Order, OrderItem
from .serializers import ProductModelSerializer, OrderModelSerializer, OrderItemModelSerializer
from django.http import Http404


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    # def get(self, request, pk):
    #     product = self.get_object(pk)
    #     serializer = ProductModelSerializer(product)
    #     return Response(serializer.data)

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        serializer = ProductModelSerializer(product)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductModelSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderModelSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderModelSerializer(order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
        serializer = OrderModelSerializer(order, data=request.data)
        if serializer.is_valid():
            print("it's valid")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderItemList(APIView):
    def get(self, request):
        order_items = OrderItem.objects.all()
        serializer = OrderItemModelSerializer(order_items, many=True)
        return Response(serializer.data)