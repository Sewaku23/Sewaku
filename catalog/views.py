from django.shortcuts import render

from .models import Product


def product_list(request):
    """
    Menampilkan seluruh produk.
    """

    products = Product.objects.select_related(
        "category"
    ).all()

    context = {
        "products": products
    }

    return render(
        request,
        "catalog/product_list.html",
        context
    )