from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name","parent")
    
    list_display = (
        "id",
        "name",
        "parent",
        "created_at",
        "updated_at",
        )
