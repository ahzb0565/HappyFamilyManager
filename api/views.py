from rest_framework.response import Response
from rest_framework import status, viewsets, decorators
from .serializers import ItemSerializer, MonthReportSerializer
from .models import Item, MonthReport
from django.shortcuts import get_object_or_404, redirect
from datetime import date, datetime
from .constants import ACCOUNT_TYPES


@decorators.api_view(http_method_names=['GET'])
def account_types(request):
    return Response(data=[_[0] for _ in ACCOUNT_TYPES], status=status.HTTP_200_OK)


class MonthReportView(viewsets.ViewSet):
    def list(self, request):
        instances = MonthReport.objects.all()
        serializer = MonthReportSerializer(instance=instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(MonthReport, pk=pk)
        serializer = MonthReportSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, day=None):
        '''
        :param date:  2017-01-01
        '''
        if day:
            day = datetime.strptime(day, "%Y-%m-%d").date()
        else:
            day = date.today()
        report, result = MonthReport.objects.get_or_create(date=day)
        return redirect('api:get-report', pk=report.date)

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

