from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer

class PrecisionAPIView(APIView):
    def post(self, request):
        pass
# Create your views here.
