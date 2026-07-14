from django.db import models
from django.conf import settings
from catalog.models import Product
from datetime import timedelta

class Rental(models.Model):
    """
    Menyimpan transaksi penyewaan.
    """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_ON_RENT = "on_rent"
    STATUS_RETURNED = "returned"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_ON_RENT, "Sedang Disewa"),
        (STATUS_RETURNED, "Dikembalikan"),
        (STATUS_COMPLETED, "Selesai"),
        (STATUS_CANCELLED, "Dibatalkan"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rentals",
        verbose_name="Penyewa"
    )

    start_date = models.DateField(
        verbose_name="Tanggal Sewa"
    )

    end_date = models.DateField(
        verbose_name="Tanggal Kembali"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        verbose_name="Status"
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Total Harga"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Rental #{self.id} - {self.user.username}"
        @property
        def rental_days(self):
            """
            Menghitung lama penyewaan.
            """

            return (self.end_date - self.start_date).days

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Rental"
        verbose_name_plural = "Rentals"

    def can_be_rented(self):
        """
        Mengecek apakah semua stok cukup.
        """

        for item in self.items.all():

            if item.quantity > item.product.stock:

                return False

        return True

    def stock_problem(self):
        """
        Mengembalikan daftar produk
        yang stoknya tidak cukup.
        """

        problems = []

        for item in self.items.all():

            if item.quantity > item.product.stock:

                problems.append(item.product.name)

        return problems

        if not rental.can_be_rented():

            messages.error(
                request,
                f"Stock tidak cukup : {rental.stock_problem()}"
            )



class RentalItem(models.Model):
    """
    Detail setiap produk yang disewa.
    """

    rental = models.ForeignKey(
        Rental,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Rental"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Produk"
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Jumlah"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Harga / Hari"
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Subtotal"
    )

    def save(self, *args, **kwargs):

            self.subtotal = self.calculate_subtotal

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
        @property
        def calculate_subtotal(self):
            """
            Menghitung subtotal setiap produk.
            """

            rental_days = self.rental.rental_days

            return self.price * self.quantity * rental_days

        @property
        def calculate_total(self):
                """
                Menghitung total seluruh produk.
                """

                total = 0

                for item in self.items.all():

                    total += item.calculate_subtotal

                return total

    class Meta:
        verbose_name = "Rental Item"
        verbose_name_plural = "Rental Items"


    
    
    

    