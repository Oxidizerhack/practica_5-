# PG2_practica_5 - API REST con Patrones de Diseño

## 📋 Descripción

API REST desarrollada con Django y Django REST Framework que implementa los patrones de diseño **Factory**, **Builder** y **Singleton** para el manejo de pedidos de café personalizados.

## 🏗️ Patrones de Diseño Implementados

### 1. **Factory Pattern** 🏭
- **¿Qué es?**: Patrón creacional que proporciona una interfaz para crear objetos sin especificar la clase exacta.
- **¿Dónde está implementado?**: `pedidos_cafe/factory.py`
- **¿Por qué se utilizó?**: Para crear diferentes tipos de café base (Espresso, Americano, Latte) sin que el código cliente necesite conocer las clases concretas.

```python
# Ejemplo de uso
cafeteria = CafeFactory.obtener_base("espresso")  # Retorna instancia de Espresso
```

### 2. **Builder Pattern** 🔨
- **¿Qué es?**: Patrón creacional que permite construir objetos complejos paso a paso.
- **¿Dónde está implementado?**: `pedidos_cafe/builder.py`
- **¿Por qué se utilizó?**: Para construir pedidos de café personalizados con ingredientes adicionales y diferentes tamaños, permitiendo flexibilidad en la configuración.

```python
# Ejemplo de uso
constructor = CafeteriaPersonalizadaBuilder(base_cafe)
director = DirectorDelCafe(constructor)
director.construir(["leche", "azucar"], "grande")
precio = constructor.obtener_precio()
```

### 3. **Singleton Pattern** 🔗
- **¿Qué es?**: Patrón creacional que garantiza que una clase tenga una sola instancia y proporciona acceso global a ella.
- **¿Dónde está implementado?**: `api_patrones/logger.py`
- **¿Por qué se utilizó?**: Para mantener un registro centralizado de logs de todas las operaciones de cálculo realizadas en el sistema.

```python
# Ejemplo de uso
logger = Registrador.instancia()  # Siempre retorna la misma instancia
logger.agregar_log("Operación realizada")
```

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/Oxidizerhack/practica_5-.git
cd PG2_practica_5
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate 
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

## 📖 Uso de la API

### Endpoints disponibles:

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/pedidos/` | Listar todos los pedidos |
| POST | `/pedidos/` | Crear nuevo pedido |
| GET | `/pedidos/{id}/` | Obtener pedido específico |
| PUT | `/pedidos/{id}/` | Actualizar pedido |
| DELETE | `/pedidos/{id}/` | Eliminar pedido |

### Ejemplo de creación de pedido:
```json
{
    "cliente": "Juan",
    "tipo_base": "espresso",
    "ingredientes": ["leche", "azucar", "canela"],
    "tamano": "grande"
}
```

### Respuesta esperada:
```json
{
    "id": 1,
    "cliente": "Jhonny",
    "tipo_base": "espresso",
    "ingredientes": ["leche", "azucar", "canela"],
    "ingredientes_texto": "leche, azucar, canela",
    "tamano": "grande",
    "fecha": "2025-07-07",
    "precio_total": 22,
    "ingredientes_finales": ["cafe espresso", "leche", "azucar", "canela"]
}
```

## 🧪 Cómo probar los patrones

### 1. **Factory Pattern**
```python
# En Django shell: python manage.py shell
from pedidos_cafe.factory import CafeFactory

# Crear diferentes tipos de café
espresso = CafeFactory.obtener_base("espresso")
americano = CafeFactory.obtener_base("americano")
latte = CafeFactory.obtener_base("latte")

print(f"Espresso: ${espresso.precio}")  # $15
print(f"Americano: ${americano.precio}")  # $12
print(f"Latte: ${latte.precio}")  # $18
```

### 2. **Builder Pattern**
```python
# Construir pedido personalizado
from pedidos_cafe.builder import CafeteriaPersonalizadaBuilder, DirectorDelCafe

base = CafeFactory.obtener_base("espresso")
constructor = CafeteriaPersonalizadaBuilder(base)
director = DirectorDelCafe(constructor)

director.construir(["leche", "azucar"], "grande")
precio = constructor.obtener_precio()  # 15 + 4 (grande) + 2 (ingredientes) = 21
```

### 3. **Singleton Pattern**
```python
# Verificar que siempre es la misma instancia
from api_patrones.logger import Registrador

logger1 = Registrador.instancia()
logger2 = Registrador.instancia()

print(logger1 is logger2)  # True - misma instancia
```

## 📊 Estructura del Proyecto

```
PG2_practica_5/
├── api_patrones/
│   ├── __init__.py
│   ├── asgi.py
│   ├── logger.py          # 🔗 Singleton Pattern
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pedidos_cafe/
│   ├── __init__.py
│   ├── admin.py           # 🔧 Admin configurado
│   ├── apps.py
│   ├── builder.py         # 🔨 Builder Pattern
│   ├── factory.py         # 🏭 Factory Pattern
│   ├── models.py          # 📋 Modelo con validación
│   ├── serializers.py     # 🔄 Serializers con patrones
│   ├── views.py           # 👁️ ViewSets
│   └── migrations/
├── manage.py
├── requirements.txt
└── README.md
```

## 🔍 Ingredientes Válidos

El sistema valida que solo se puedan usar los siguientes ingredientes:
- `leche`
- `azucar`
- `canela`
- `vainilla`
- `chocolate`
- `crema`
- `caramelo`
- `nuez`
- `almendra`
- `coco`

## 💰 Cálculo de Precios

### Precios base:
- **Espresso**: $15
- **Americano**: $12
- **Latte**: $18

### Costos adicionales:
- **Tamaño pequeño**: +$0
- **Tamaño mediano**: +$2
- **Tamaño grande**: +$4
- **Cada ingrediente extra**: +$1

### Fórmula:
```
Precio Final = Precio Base + Costo Tamaño + (Ingredientes × $1)
```

## 🔒 Validaciones

1. **Tipo de café**: Solo acepta "espresso", "americano", "latte"
2. **Tamaño**: Solo acepta "pequeno", "mediano", "grande"
3. **Ingredientes**: Solo acepta ingredientes de la lista válida
4. **Cliente**: Campo obligatorio, máximo 100 caracteres

## 🧑‍💻 Tecnologías Utilizadas

- **Django 5.2.4**: Framework web
- **Django REST Framework 3.16.0**: API REST
- **SQLite**: Base de datos
- **Python 3.x**: Lenguaje de programación

## 📝 Logs del Sistema

El sistema registra automáticamente:
- Cálculos de precios
- Obtención de ingredientes finales
- Errores en procesamiento
- Operaciones realizadas

Los logs se pueden consultar accediendo a la instancia del Singleton:
```python
logger = Registrador.instancia()
print(logger.obtener_logs())
```

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza los cambios
4. Envía un pull request

## 📄 Licencia

Este proyecto es desarrollado con fines educativos para la materia de Programación II.