from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import PaymentMethodForm, PaymentProofForm
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

        if payment.payment_method == Payment.METHOD_TRANSFER:

            return redirect(
                "upload_payment",
                payment_id=payment.id,
            )

        return redirect(
            "cash_information",
            payment_id=payment.id,
        )

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


@login_required
def upload_payment(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        rental__user=request.user,
    )

    if request.method == "POST":

        form = PaymentProofForm(
            request.POST,
            request.FILES,
            instance=payment,
        )

        if form.is_valid():

            payment = form.save(commit=False)

            payment.status = Payment.STATUS_WAITING

            payment.save()

            return redirect("my_rentals")

    else:

        form = PaymentProofForm(
            instance=payment,
        )

    context = {
        "payment": payment,
        "form": form,
    }

    return render(
        request,
        "payments/upload_payment.html",
        context,
    )


@login_required
def cash_information(request, payment_id):

    payment = get_object_or_404(
        Payment,
        id=payment_id,
        rental__user=request.user,
    )

    if request.method == "POST":

        return redirect("my_rentals")

    context = {

        "payment": payment,

    }

    return render(

        request,

        "payments/cash_information.html",

        context,

    )