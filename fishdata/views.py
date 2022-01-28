from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import fish
from .serializers import fishSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class fishList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request):
        fish1 = fish.objects.all().order_by('-timestamp')
        serializer = fishSerializer(fish1, many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = fishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        