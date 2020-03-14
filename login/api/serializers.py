from rest_framework.serializers import ModelSerializer
from login.models import Register

class RegisterSerializers(ModelSerializer):
    class Meta:
        model = Register
        fields = ('name', 'password', 'confirm_password', 'date_of_birth', 'username', 'cpf')