from django.db import models
from rentals.models import Rental


class Payment(models.Model):

    STATUS_UNPAID = "unpaid"
    STATUS_WAITING = "waiting"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_UNPAID, "Belum Dibayar"),
        (STATUS_WAITING, "Menunggu Verifikasi"),
        (STATUS_APPROVED, "Disetujui"),
        (STATUS_REJECTED, "Ditolak"),
        (STATUS_CANCELLED, "Dibatalkan"),
    ]

    METHOD_TRANSFER = "transfer"
    METHOD_CASH = "cash"

    METHOD_CHOICES = [
        (METHOD_TRANSFER, "Transfer Bank"),
        (METHOD_CASH, "Cash"),
    ]

    rental = models.OneToOneField(
        Rental,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES,
        blank=True,
        null=True,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    proof = models.ImageField(
        upload_to="payments/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_UNPAID
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.rental.user.username}"