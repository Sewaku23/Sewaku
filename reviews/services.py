from django.core.exceptions import PermissionDenied
from .exceptions import ReviewError
from rentals.models import Rental
from .models import Review


def can_review(user, rental_item):
    """
    Mengecek apakah user boleh memberikan review.
    """

    if rental_item.rental.user != user:
        raise ReviewError(
            "Anda bukan penyewa produk ini."
        )

    if rental_item.rental.status != Rental.STATUS_COMPLETED:
        raise ReviewError(
            "Produk belum selesai disewa."
        )

    if hasattr(rental_item, "review"):
        raise ReviewError(
            "Produk ini sudah direview."
        )

    return True

def create_review(user, rental_item, form):
    """
    Membuat review baru.
    """

    can_review(user, rental_item)

    review = form.save(commit=False)

    review.user = user

    review.rental_item = rental_item

    review.save()

    return review

def update_review(review, form):
    """
    Mengubah review.
    """

    review.rating = form.cleaned_data["rating"]

    review.comment = form.cleaned_data["comment"]

    review.save()

    return review