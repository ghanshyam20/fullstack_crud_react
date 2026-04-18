from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET', 'POST'])
def items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

@api_view(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
        item.delete()
        return Response({"message": "deleted"})
    except Item.DoesNotExist:
        return Response({"error": "not found"}, status=404)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET', 'POST'])
def items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

@api_view(['PUT'])
def update_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return Response({"error": "not found"}, status=404)

    serializer = ItemSerializer(item, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)
    

@api_view(['DELETE'])
def delete_item(request, id):
    try:
        item = Item.objects.get(id=id)
        item.delete()
        return Response({"message": "deleted"})
    except Item.DoesNotExist:
        return Response({"error": "not found"}, status=404)