from django.contrib import admin
from pedidos_cafe.models import PedidoCafe

@admin.register(PedidoCafe)
class PedidoCafeAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'tipo_base', 'tamano', 'fecha']
    list_filter = ['tipo_base', 'tamano', 'fecha']
    search_fields = ['cliente']
    readonly_fields = ['fecha']
    
    fieldsets = (
        ('Información del Pedido', {
            'fields': ('cliente', 'tipo_base', 'tamano')
        }),
        ('Personalización', {
            'fields': ('ingredientes',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha',),
            'classes': ('collapse',)
        })
    )