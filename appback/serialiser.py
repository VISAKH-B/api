from rest_framework import serializers
from .models import tbl_todo
class tbl_todoSerializer(serializers.ModelSerializer):
    class Meta:
        model=tbl_todo
        fields='__all__'