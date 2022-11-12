from typing import NoReturn
from rest_framework.serializers import ModelSerializer
from .models import User


class NoteSerialize(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'