from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonthlyReportSerializer
from .models import MonthlyReport
from django.shortcuts import get_object_or_404


class MonthlyReportView(APIView):

    def get(self, request, pk=None):
        if pk:
            instance = get_object_or_404(MonthlyReport, pk=pk)
            many = False
        else:
            instance = MonthlyReport.objects.all()
            many = True
        serializer = MonthlyReportSerializer(instance=instance, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MonthlyReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response({'error': serializer.errors}, status=400)