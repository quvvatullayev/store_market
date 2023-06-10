from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from ..models import (
    Order,
    User
)
from ..serializers import (
    OrderSerializer,
    UserSerializer
)

class AddOrder(APIView):
    def post(self, request: Request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Order created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'Order not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class OrderList(APIView):
    def get(self, request: Request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({
            'status': True,
            'message': 'Order list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class GetOrder(APIView):
    def get(self, request: Request, user_id):
        order = Order.objects.get(user=user_id)
        serializer = OrderSerializer(order)
        return Response({
            'status': True,
            'message': 'Order',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class GetOrder_by_chat_id(APIView):
    def get(self, request: Request, chat_id):
        user_data = User.objects.get(chat_id = chat_id)
        user = UserSerializer(user_data)
        
        order_data = Order.objects.filter(user = user['id'])
        order = OrderSerializer(order_data, many=True)

        return Response({
                'status': True,
                'message': 'Order by chat id successfully',
                'data': order.data
            }, status=status.HTTP_200_OK)

    
class UpdateOrder(APIView):
    def post(self, request: Request):
        data = request.data
        order = Order.objects.get(id=data['id'])
        serializer = OrderSerializer(order, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Order updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': 'Order not updated',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteOrder(APIView):
    def post(self, request: Request):
        data = request.data
        order = Order.objects.get(id=data['id'])
        order.delete()
        return Response({
            'status': True,
            'message': 'Order deleted successfully',
            'data': []
        }, status=status.HTTP_200_OK)
    
class AddOrderList(APIView):
    def post(self, request: Request):
        data = request.data
        response = []
        for item in data:
            serializer = OrderSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                response.append(serializer.data)
        return Response({
            'status': True,
            'message': 'Order list created successfully',
            'data': response
        }, status=status.HTTP_201_CREATED)