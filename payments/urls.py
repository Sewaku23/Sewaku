from django.urls import path

from . import views

urlpatterns = [
    path(
        "checkout/<int:payment_id>/",
        views.checkout_summary,
        name="checkout_summary",
    ),
]