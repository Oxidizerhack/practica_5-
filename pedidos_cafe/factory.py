# pedidos_cafe/factory.py

class Espresso:
    def __init__(self):
        self.precio = 15
        self.ingredientes = ["cafe espresso"]

class Americano:
    def __init__(self):
        self.precio = 12
        self.ingredientes = ["cafe americano"]

class Latte:
    def __init__(self):
        self.precio = 18
        self.ingredientes = ["cafe espresso", "leche"]

class CafeFactory:
    @staticmethod  
    def obtener_base(tipo_base):
        if tipo_base == "espresso":
            return Espresso()
        elif tipo_base == "americano":
            return Americano()
        elif tipo_base == "latte":  
            return Latte()
        else:
            raise ValueError(f"Tipo de café no soportado: {tipo_base}")