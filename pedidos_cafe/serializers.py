# pedidos_cafe/serializers.py

from rest_framework import serializers
from pedidos_cafe.models import PedidoCafe
from pedidos_cafe.factory import CafeFactory
from pedidos_cafe.builder import CafeteriaPersonalizadaBuilder, DirectorDelCafe
from api_patrones.logger import Registrador


class PedidoCafeSerializer(serializers.ModelSerializer):
    precio_total = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()
    ingredientes_texto = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCafe
        fields = [
            "id",
            "cliente",
            "tipo_base",
            "ingredientes",
            "ingredientes_texto",
            "tamano",
            "fecha",
            "precio_total",
            "ingredientes_finales"
        ]
    def get_ingredientes_texto(self, obj):
        return ", ".join(obj.ingredientes)

    def get_precio_total(self, obj):
        cafeteria = CafeFactory.obtener_base(obj.tipo_base)
        constructor = CafeteriaPersonalizadaBuilder(cafeteria)
        director = DirectorDelCafe(constructor)
        director.construir(obj.ingredientes, obj.tamano)

        lista_ingredientes = [i.strip() for i in obj.ingredientes.split(",") if i.strip()]
        director.construir(lista_ingredientes, obj.tamano)


    def get_ingredientes_finales(self, obj):
        cafeteria = CafeFactory.obtener_base(obj.tipo_base)
        constructor = CafeteriaPersonalizadaBuilder(cafeteria)
        director = DirectorDelCafe(constructor)
        director.construir(obj.ingredientes, obj.tamano)

        lista_ingredientes = [i.strip() for i in obj.ingredientes.split(",") if i.strip()]
        director.construir(lista_ingredientes, obj.tamano)

        Registrador.instancia().agregar_log(f"[ingredientes_finales] Obtenidos para el pedido {obj.id}")
        return constructor.obtener_ingredientes_finales()
