from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ItemSerializer, MonthReportSerializer
from .models import Item, MonthReport
from django.shortcuts import get_object_or_404
from datetime import date


class MonthReportView(viewsets.ViewSet):
    def list(self, request):
        instances = MonthReport.objects.all()
        serializer = MonthReportSerializer(instance=instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(MonthReport, pk=pk)
        serializer = MonthReportSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        today = date.today()
        if MonthReport.objects.filter(date=today):
            return Response({'error': 'Report exists for date {}'.format(today)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MonthReportSerializer(data={'date': date.today()})
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

    def delete(self, request, pk=None):
        instance = get_object_or_404(MonthReport, pk=pk)
        instance.delete()
        return Response(status=200)


class ItemView(viewsets.ViewSet):

    def list(self, request):
        instances = Item.objects.all()
        serializer = ItemSerializer(instance=instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response({'error': serializer.errors}, status=400)

    def delete(self, request, pk=None):
        instance = get_object_or_404(Item, pk=pk)
        instance.delete()
        return Response(status=200)

