from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet
from .serializers import FundSerializer
from .models.Fund import Fund


class CurrentUser(APIView):
    def get(self, request):
        return Response(data={
            'name': 'Serati Ma',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png',
            'userid': '00000001',
            'email': 'antdesign@alipay.com',
            'signature': '海纳百川，有容乃大',
            'title': '交互专家',
            'group': '蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED',
            'tags': [
                {
                    'key': '0',
                    'label': '很有想法的',
                },
            ],
            'notifyCount': 12,
            'unreadCount': 11,
            'country': 'China',
            'geographic': {
                'province': {
                    'label': '浙江省',
                    'key': '330000',
                },
                'city': {
                    'label': '杭州市',
                    'key': '330100',
                },
            },
            'address': '西湖区工专路 77 号',
            'phone': '0752-268888888',
        }, status=HTTP_200_OK)


class AuthRoutes(APIView):
    def get(self, request):
        return Response(
            data={
                '/form/advanced-form': {'authority': ['admin', 'user']},
            },
            status=HTTP_200_OK
        )


class FundViewSet(ModelViewSet):
    serializer_class = FundSerializer
    queryset = Fund.objects.all()
