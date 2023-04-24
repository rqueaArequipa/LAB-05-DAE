from django.contrib import admin
from .models import Categoria, Producto, Cliente

admin.site.register(Categoria)
#admin.site.register(Producto)
#admin.site.register(Cliente)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')
    list_display_links = ('id',)
    list_editable = ('nombre', 'precio', 'stock')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'telefono', 'direccion', 'email', 'nac_date', 'pud_date')
    list_display_links = ('id',)
    list_editable = ('nombre', 'apellido', 'dni', 'telefono', 'direccion', 'email', 'nac_date')
    search_fields = ('nombre','dni')
