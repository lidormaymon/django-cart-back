from django.shortcuts import render
from .seralizer import CartItemSerializer, DeliveriesSerializer, ProductSerializer, OrderSerializer
from .models import Orders, Deliveries, Product
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(req):
    return Response('hello')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def about(req):
    return Response('welcome motek')


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(username= request.data["username"],password=request.data['password'],is_staff=1,is_superuser=1)
    return Response({"reg":"test"})



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data['message'] = 'Login successful.'
        else:
            response.data['message'] = 'Invalid login credentials.'
        return response

# <---------------------------------------------------------------Products Entry Points --------------------------------------->
class ProductViewSet(APIView):
    def get(self, request):
        my_model = Product.objects.all()
        serializer = ProductSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        serializer = ProductSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# <---------------------------------------------- Orders Entry Points ------------------------------------------->
class OrderViewSet(APIView):
    def get(self, request):
        my_model = Orders.objects.all()
        serializer = OrderSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Orders.objects.get(pk=pk)
        serializer = OrderSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Orders.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# <--------------------------------------------------- Cart Entry Points ------------------------------------------->
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart_items = request.data
        print(cart_items)
        serializer = CartItemSerializer(data=request.data,  context={'user': request.user},many=True)
        if serializer.is_valid():
            cart_items = serializer.save()
        #     # Process the cart items as needed
        #     # ...
            return Response("Cart items received and processed successfully.")
        else:
            return Response(serializer.errors, status=400)
        

 # <--------------------------------------------------- Deliveres Entry Points ------------------------------------------->   
class DeliveriesViewSet(APIView):
    def get(self, request):
        my_model = Deliveries.objects.all()
        serializer = DeliveriesSerializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliveriesSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Deliveries.objects.get(pk=pk)
        serializer = DeliveriesSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk):
        my_model = Product.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


