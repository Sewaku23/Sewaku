from django.urls import path

from . import views

urlpatterns = [
    path(
        "checkout/<int:payment_id>/",
        views.checkout_summary,
        name="checkout_summary",
    ),

    path(
    "upload/<int:payment_id>/",
    views.upload_payment,
    name="upload_payment",
    ),
]