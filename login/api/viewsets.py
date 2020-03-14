from rest_framework.viewsets import ModelViewSet
from login.models import Register
from .serializers import RegisterSerializers

class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers