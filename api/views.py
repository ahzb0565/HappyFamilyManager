from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CashAndBackupAccountSerializer
from .models import CashAndBackupAccount
from django.shortcuts import get_object_or_404


class CashAndBackupAccountView(APIView):

    def get(self, request, pk=None):
        if pk:
            instance = get_object_or_404(CashAndBackupAccount, pk=pk)
            many = False
        else:
            instance = CashAndBackupAccount.objects.all()
            many = True
        serializer = CashAndBackupAccountSerializer(instance, many=many)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CashAndBackupAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response({'error': serializer.errors}, status=400)
