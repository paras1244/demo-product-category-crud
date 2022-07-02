from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    
    list_display = (
        "id",
        "name",
        "price",
        "created_at",
        "updated_at",
        )
