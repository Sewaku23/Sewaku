from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    Model kategori produk outdoor.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Tenda"
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    description = models.TextField(
        blank=True,
        verbose_name="Tenda"
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