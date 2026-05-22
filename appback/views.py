from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import tbl_todo
from .serialiser import tbl_todoSerializer



class tbl_todolst(APIView):
    def get(self, request):
        x=tbl_todo.objects.all()
        y=tbl_todoSerializer(x,many=True)
        return Response(y.data)


    def post(self, request):
        x=tbl_todoSerializer(data=request.data)
        if x.is_valid():
            x.save()
            return Response(x.data)
        return Response(x.errors)

    def put(self, request, pk):
        x=tbl_todo.objects.get(id=pk)
        y=tbl_todoSerializer(x,data=request.data)
        if y.is_valid():
            y.save()
            return Response(y.data)
        return Response(y.errors)


    def patch(self, request, pk):
        x=tbl_todo.objects.get(id=pk)
        y=tbl_todoSerializer(x,data=request.data,partial=True)
        if y.is_valid():
            y.save()
            return Response(y.data)
        return Response(y.errors)

    def delete(self, request, pk):
        x=tbl_todo.objects.get(id=pk)
        x.delete()
        return Response("deleted successfully")
    