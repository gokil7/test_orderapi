from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from rest_framework.views import APIView
from .serializers import ContactedSerializer, OrderSerializer
from django.db.models import Max


# Create your views here.


@api_view(['GET'])
def orderapi(request):

    orderapi_urls  = {
        'View Orders' : '/order-lists/',
        'View Latest Order' : '/new-order/',
        'View Specific Order' : '/order-detail/<str:pk>',
        'Create Order' : '/create-order/',
        'Update Order' : '/update-order/<str:pk>',
        'Delete Order' : '/delete-order/<str:pk>',
    }
    return Response(orderapi_urls)


@api_view(['GET'])
def orderLists(request):
    orderlist = Order.objects.all()
    serializer = OrderSerializer(orderlist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orderDetails(request, pk):
    orderlist = Order.objects.get(id = pk)
    serializer = OrderSerializer(orderlist, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def newOrder(request):
    orderlist = Order.objects.filter().order_by("-id")[0]
    serializer = OrderSerializer(orderlist, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def customerContacted(request):
    serializer = ContactedSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateOrder(request, pk):
    orderlist = Order.objects.get(id = pk)
    serializer = OrderSerializer(instance=orderlist, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteOrder(request, pk):
    orderlist = Order.objects.get(id = pk)
    orderlist.delete()
    return Response("Item Successfully Deleted")

