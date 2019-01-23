from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class Hello(APIView):
    def get(self, request):
        return Response(data={'result': 'Hi Bob!'}, status=HTTP_200_OK)