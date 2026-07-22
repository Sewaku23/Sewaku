from django import forms

from .models import Payment


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["payment_method"]

        widgets = {
            "payment_method": forms.RadioSelect,
        }