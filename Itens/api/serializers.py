from rest_framework.serializers import ModelSerializer
from Itens.models import Item

class ItemSerializers(ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'description', 'user')