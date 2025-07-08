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
        if isinstance(obj.ingredientes, list):
            return ", ".join(obj.ingredientes)
        return ""

    def get_precio_total(self, obj):
        try:
            # Usar Factory para crear el café base
            cafeteria = CafeFactory.obtener_base(obj.tipo_base)
            
            # Usar Builder para construir el pedido completo
            constructor = CafeteriaPersonalizadaBuilder(cafeteria)
            director = DirectorDelCafe(constructor)
            director.construir(obj.ingredientes, obj.tamano)
            
            # Registrar la operación con Singleton
            Registrador.instancia().agregar_log(f"[precio_total] Calculado para pedido {obj.id}: ${constructor.obtener_precio()}")
            
            return constructor.obtener_precio()  
        except Exception as e:
            Registrador.instancia().agregar_log(f"[ERROR] No se pudo calcular precio para pedido {obj.id}: {str(e)}")
            return 0

    def get_ingredientes_finales(self, obj):
        try:
            # Usar Factory para crear el café base
            cafeteria = CafeFactory.obtener_base(obj.tipo_base)
            
            # Usar Builder para construir el pedido completo
            constructor = CafeteriaPersonalizadaBuilder(cafeteria)
            director = DirectorDelCafe(constructor)
            director.construir(obj.ingredientes, obj.tamano)
            
            # Registrar la operación con Singleton
            Registrador.instancia().agregar_log(f"[ingredientes_finales] Obtenidos para el pedido {obj.id}")
            
            return constructor.obtener_ingredientes_finales()
        except Exception as e:
            Registrador.instancia().agregar_log(f"[ERROR] No se pudieron obtener ingredientes finales para pedido {obj.id}: {str(e)}")
            return []