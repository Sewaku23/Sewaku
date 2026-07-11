from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Category di Django Admin.
    """

    list_display = (
        "name",
        "slug",
        "created_at",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Product di Django Admin.
    """

    list_display = (
        "name",
        "category",
        "brand",
        "price_per_day",
        "stock",
        "created_at",
    )

    list_filter = (
        "category",
        "brand",
    )

    search_fields = (
        "name",
        "brand",
        "description",
    )

    list_editable = (
        "stock",
    )

    list_select_related = (
        "category",
    )

    ordering = (
        "category",
        "name",
    )

    prepopulated_fields = {
    "slug": ("name",)
    }

    list_per_page = 15