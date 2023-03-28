from django.contrib import admin
from . models import *
# Register your models here.
# admin.site.register(Purchase)
# admin.site.register(Stock)
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id','item','quantity']

@admin.register(Stock)
class STokAdmin(admin.ModelAdmin):
    list_display = ['id','available_item','available_quantity']    