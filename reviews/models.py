from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from rentals.models import RentalItem


class Review(models.Model):
    """
    Review dan rating untuk setiap produk
    yang telah disewa pengguna.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rental_item = models.OneToOneField(
        RentalItem,
        on_delete=models.CASCADE,
        related_name="review",
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        verbose_name="Rating",
    )

    comment = models.TextField(
        verbose_name="Review"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return (
            f"{self.user.username} | "
            f"{self.rental_item.product.name} | "
            f"{self.rating}⭐"
        )