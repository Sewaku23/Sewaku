from django.contrib import admin

from .models import Rental, RentalItem


@admin.action(description="Approve Rental")
def approve_rental(modeladmin, request, queryset):

    for rental in queryset:
        rental.approve()


@admin.action(description="Complete Rental")
def complete_rental(modeladmin, request, queryset):

    for rental in queryset:
        rental.complete()


class RentalItemInline(admin.TabularInline):
    model = RentalItem
    extra = 0


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "status",
        "start_date",
        "end_date",
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

    actions = (
        approve_rental,
        complete_rental,
    )

    inlines = (
        RentalItemInline,
    )


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

    ordering = (
        "-id",
    )