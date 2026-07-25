from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from rentals.models import RentalItem

from .exceptions import ReviewError
from .forms import ReviewForm
from .services import create_review


@login_required
def create_review_view(request, rental_item_id):
    print("MASUK KE CREATE REVIEW")
    rental_item = get_object_or_404(
        RentalItem,
        pk=rental_item_id,
    )

    if request.method == "POST":

        form = ReviewForm(request.POST)

        if form.is_valid():

            try:

                create_review(
                    request.user,
                    rental_item,
                    form,
                )

                messages.success(
                    request,
                    "Review berhasil ditambahkan."
                )

                return redirect(
                    "product_detail",
                    slug=rental_item.product.slug,
                )

            except ReviewError as e:

                messages.error(
                    request,
                    str(e)
                )

    else:

        form = ReviewForm()

    return render(
        request,
        "reviews/add_review.html",
        {
            "form": form,
            "rental_item": rental_item,
        },
    )