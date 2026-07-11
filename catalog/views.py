from django.shortcuts import render, get_object_or_404

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


def product_detail(request, pk):
    """
    Menampilkan detail satu produk.
    """

    product = get_object_or_404(
        Product.objects.select_related("category"),
        pk=pk
    )

    context = {
        "product": product
    }

    return render(
        request,
        "catalog/product_detail.html",
        context
    )