from django.contrib import admin
from .models import Brand, MobilePhone

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(MobilePhone)
class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model_name', 'price', 'storage', 'ram', 'condition', 'in_stock', 'added_on')
    list_filter = ('brand', 'condition', 'in_stock')
    search_fields = ('model_name',)
