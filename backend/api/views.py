from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    data = [{"id": i.id, "name": i.name} for i in items]
    return Response(data)