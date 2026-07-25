from django.shortcuts import render, get_object_or_404

from .models import Product, Category

from django.core.paginator import Paginator

from django.db.models import Q

def product_list(request):
    """
    Menampilkan daftar produk
    beserta search, filter dan pagination.
    """

    query = request.GET.get("q", "")

    category_slug = request.GET.get("category")

    products = Product.objects.select_related(
        "category"
    )

    categories = Category.objects.all()

    if category_slug:

        products = products.filter(
            category__slug=category_slug
        )

    if query:

        products = products.filter(

        Q(name__icontains=query)
        |
        Q(brand__icontains=query)
        |
        Q(category__name__icontains=query)
         )
        

    paginator = Paginator(products, 9)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "products": page_obj,

        "page_obj": page_obj,

        "categories": categories,

        "selected_category": category_slug,

        "query": query,

    }

    return render(
        request,
        "catalog/product_list.html",
        context
    )

def product_detail(request, slug):
    """
    Menampilkan detail satu produk.
    """

    product = get_object_or_404(
        Product.objects.select_related(
            "category"
        ).prefetch_related(
            "rental_items__review",
            "rental_items__review__user",
        ),
        slug=slug,
    )

    reviews = []

    for item in product.rental_items.all():

        if hasattr(item, "review"):

            reviews.append(item.review)

    context = {
    "product": product,
    "reviews": reviews,
    }

    return render(
        request,
        "catalog/product_detail.html",
        context
    )

