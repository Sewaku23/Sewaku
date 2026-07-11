from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    Model kategori produk outdoor.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nama Kategori"
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        verbose_name="Deskripsi"
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Contoh: tent, mountain, backpack"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        """
        Otomatis membuat slug dari nama kategori.
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """
    Model produk outdoor.
    """

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Kategori"
    )

    name = models.CharField(
        max_length=200,
        verbose_name="Nama Produk"
    )

    brand = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Merek"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        verbose_name="Slug"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Deskripsi"
    )

    price_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Harga / Hari"
    )

    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Stok"
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Foto Produk"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:

        ordering = ["name"]

        verbose_name = "Product"

        verbose_name_plural = "Products"
    
    def save(self, *args, **kwargs):

        if not self.slug:

            self.slug = slugify(self.name)

        super().save(*args, **kwargs)