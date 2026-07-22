from django.contrib import admin
from django.utils.html import format_html

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "rental",
        "payment_method",
        "proof_status",
        "amount",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "payment_method",
    )

    search_fields = (
        "rental__user__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "proof_preview",
    )

    fieldsets = (
        (
            "Informasi Pembayaran",
            {
                "fields": (
                    "rental",
                    "payment_method",
                    "amount",
                    "status",
                )
            },
        ),
        (
            "Bukti Pembayaran",
            {
                "fields": (
                    "proof",
                    "proof_preview",
                )
            },
        ),
        (
            "Informasi Sistem",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    @admin.display(description="Bukti")
    def proof_status(self, obj):

        if obj.payment_method == Payment.METHOD_CASH:
            return "-"

        if obj.proof:
            return "✅ Ada"

        return "❌ Belum Upload"

    @admin.display(description="Preview Bukti")
    def proof_preview(self, obj):

        if obj.proof:

            return format_html(
                '<img src="{}" style="max-height:300px;border-radius:10px;" />',
                obj.proof.url,
            )

        return "Belum ada bukti pembayaran."