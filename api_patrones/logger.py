# api_patrones/logger.py

class _Registrador:
    def __init__(self):
        self.logs = []

    def agregar_log(self, mensaje):
        print(mensaje)  # Para mostrar en consola
        self.logs.append(mensaje)

    def obtener_logs(self):
        return self.logs


class Registrador:
    _instancia = None

    @classmethod
    def instancia(cls):
        if cls._instancia is None:
            cls._instancia = _Registrador()
        return cls._instancia

