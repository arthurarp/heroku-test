from rest_framework.viewsets import ModelViewSet
from Itens.models import Item
from .serializers import ItemSerializers

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers