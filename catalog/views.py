from django.shortcuts import render, get_object_or_404

from .models import Product

from django.core.paginator import Paginator

def product_list(request):
    """
    Menampilkan daftar produk beserta fitur pencarian dan pagination.
    """

    query = request.GET.get("q", "")

    products = Product.objects.select_related("category")

    if query:
        products = products.filter(
            name__icontains=query
        )

    paginator = Paginator(products, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "products": page_obj,
        "query": query,
    }

    return render(
        request,
        "catalog/product_list.html",
        context,
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