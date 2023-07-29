from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger.renderers import SwaggerUIRenderer

from xnara_app.models import Xnara
from xnara_app.serializer import XnaraSerializer
import requests

from xnara_app.log import log_api_info, log_api_error

def transform(json_data, pack_num):
    """Transforming the Json Data returned in response from Xnara Mock API"""
    result = {}
    for i in range(len(json_data)):
        result['id'] = json_data[i]['id']
        result['customer_id'] = json_data[i]['customer_id']
        pack_data = []
        for data in json_data[i]['pack_data']:
            list_data = data['ingredient'] + ' ' + str(data['quantity']) + data['unit']
            pack_data.append(list_data)
        result[f'pack{pack_num}'] = pack_data

    return result

def request_pack(customer_id, pack_num):
    """Calling Xnara Mock API to get the data linked to Customer Id"""
    try:
        req = requests.get(url = f'https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack{int(pack_num)}')
        json_data = req.json()
        json_data = [i for i in json_data if int(i['customer_id']) == customer_id]
        if not json_data:
            raise KeyError('customer_id not found')
        transformed_data = transform(json_data, pack_num)
        return transformed_data
    except Exception as e:
        log_api_error.info(str(e))
        raise e
    

class TestAPIView(ModelViewSet):


    queryset = Xnara.objects.all()
    serializer_class = XnaraSerializer


    def list(self, request, *args, **kwargs):
        customer_id = request.data.get('customer_id')
        try:
            pack1 = request_pack(customer_id, 1)
            pack2 = request_pack(customer_id, 2)
        except Exception as e:
            return Response({'Error':str(e)})
        pack1['pack2'] = pack2['pack2']

        log_api_info.info(f"This customer id{customer_id} is Logged")

        return Response(pack1)
    

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get('customer_id')
        try:
            pack1 = request_pack(customer_id, 1)
            pack2 = request_pack(customer_id, 2)
        except Exception as e:
            return Response({'Error':str(e)})
        pack1['pack2'] = pack2['pack2']

        log_api_info.info(f"This customer id{customer_id} is Logged")


        return Response(pack1)
    