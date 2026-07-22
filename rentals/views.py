from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from catalog.models import Product
from payments.models import Payment
from .forms import RentalForm
from .models import Rental, RentalItem


@login_required
def create_rental(request, product_id):

    product = get_object_or_404(
        Product,
        pk=product_id
    )

    if request.method == "POST":

        form = RentalForm(request.POST)

        if form.is_valid():

            rental = form.save(commit=False)

            rental.user = request.user

            rental.save()

            item = RentalItem.objects.create(

                    rental=rental,

                    product=product,

                    quantity=1,

                    price=product.price_per_day,

                )

            # Hitung total pembayaran
            rental.total_price = item.subtotal
            rental.save(update_fields=["total_price"])

            # Buat data pembayaran otomatis
            payment = Payment.objects.create(
                rental=rental,
                amount=rental.total_price,
            )

            return redirect(
                "checkout_summary",
                payment_id=payment.id,
            )

    else:

        form = RentalForm()

    context = {

        "form": form,

        "product": product,

    }

    return render(

        request,

        "rentals/rental_form.html",

        context,

    )


@login_required
def my_rentals(request):

    rentals = Rental.objects.filter(
        user=request.user
    ).prefetch_related(
        "items__product"
    ).order_by("-created_at")

    return render(
        request,
        "rentals/my_rentals.html",
        {
            "rentals": rentals,
        },
    )