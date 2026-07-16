from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from catalog.models import Product
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

            RentalItem.objects.create(

                rental=rental,

                product=product,

                quantity=1,

                price=product.price_per_day,

            )

            return redirect("home")

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