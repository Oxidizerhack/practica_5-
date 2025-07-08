# pedidos_cafe/builder.py

# pedidos_cafe/builder.py

# builder.py

# pedidos_cafe/builder.py

import json

class CafeteriaPersonalizadaBuilder:
    def __init__(self, base):
        self.base = base
        self.ingredientes_extra = []
        self.tamano = "pequeno"

    def construir(self, ingredientes, tamano):
        # Asegurar que ingredientes siempre sea una lista
        if isinstance(ingredientes, str):
            try:
                ingredientes = json.loads(ingredientes)
            except json.JSONDecodeError:
                ingredientes = [ingredientes]
        self.ingredientes_extra = ingredientes
        self.tamano = tamano

    def obtener_precio(self):
        precio_base = self.base.precio
        precio_tamano = {"pequeno": 0, "mediano": 2, "grande": 4}
        precio_ingredientes = 1 * len(self.ingredientes_extra)
        return precio_base + precio_tamano.get(self.tamano, 0) + precio_ingredientes

    def obtener_ingredientes_finales(self):
        return self.base.ingredientes + list(self.ingredientes_extra)


class DirectorDelCafe:
    def __init__(self, builder):
        self.builder = builder

    def construir(self, ingredientes, tamano):
        self.builder.construir(ingredientes, tamano)

