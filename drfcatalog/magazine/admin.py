from django.contrib import admin
from .models import *


class WatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_active')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'product', 'quantity')


admin.site.register(Watch, WatchAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketItem, BasketItemAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
