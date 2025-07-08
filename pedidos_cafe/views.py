from rest_framework import viewsets
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.serializers import PedidoCafeSerializer

class PedidoCafeViewSet(viewsets.ModelViewSet):
    queryset = PedidoCafe.objects.all()
    serializer_class = PedidoCafeSerializer
