from django.shortcuts import render, get_object_or_404

from .models import Product


def product_list(request):
    """
    Menampilkan daftar produk dan mendukung pencarian.
    """

    query = request.GET.get("q", "")

    products = Product.objects.select_related(
        "category"
    )

    if query:
        products = products.filter(
            name__icontains=query
        )

    context = {
        "products": products,
        "query": query,
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