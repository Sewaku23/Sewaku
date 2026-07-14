from django.contrib import admin
from .models import Rental, RentalItem


class RentalItemInline(admin.TabularInline):
    model = RentalItem
    extra = 0


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "start_date",
        "end_date",
        "status",
        "total_price",
    )

    list_filter = (
        "status",
        "start_date",
        "end_date",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    ordering = (
        "-created_at",
    )

    inlines = [
        RentalItemInline,
    ]


@admin.register(RentalItem)
class RentalItemAdmin(admin.ModelAdmin):

    list_display = (
        "rental",
        "product",
        "quantity",
        "price",
        "subtotal",
    )

    search_fields = (
        "product__name",
    )