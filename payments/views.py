from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import PaymentMethodForm
from .models import Payment


@login_required
def checkout_summary(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        rental__user=request.user,
    )

    if request.method == "POST":

        form = PaymentMethodForm(
            request.POST,
            instance=payment,
        )

        if form.is_valid():

            form.save()

        return redirect("my_rentals")

    else:

        form = PaymentMethodForm(
            instance=payment,
        )

    context = {

        "payment": payment,

        "rental": payment.rental,

        "form": form,

    }

    return render(

        request,

        "payments/checkout_summary.html",

        context,

    )