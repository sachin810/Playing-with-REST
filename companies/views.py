from django.shortcuts import render
from .models import Stock
from rest_framework import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StockSerializer
from rest_framework import status


class StockView(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializers = StockSerializer(stocks, many=True)
        return Response(serializers.data)

    def post(self):
        pass
