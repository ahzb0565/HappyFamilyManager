from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class API1(APIView):

    def get(self, request):
        return Response({'result': 'Pass'}, status=status.HTTP_200_OK)