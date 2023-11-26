from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
import predict

class PrecisionAPIView(APIView):
    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            prediction = predict.predict_time(serializer.data)
            return Response(
                {
                    "data" : prediction
                }, status=status.HTTP_200_OK
            )
# Create your views here.
