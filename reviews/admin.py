from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "get_product",
        "rating",
        "created_at",
    )

    list_filter = (
        "rating",
        "created_at",
    )

    search_fields = (
        "user__username",
        "rental_item__product__name",
    )

    ordering = (
        "-created_at",
    )

    @admin.display(description="Product")
    def get_product(self, obj):
        return obj.rental_item.product.name