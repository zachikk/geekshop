from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(verbose_name="имя категории", max_length=64, unique=True)
    link = models.CharField(verbose_name="ссылка", max_length=64)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"menu category with id - {self.pk}"

    class Meta:
        verbose_name = "Меню категории"
        verbose_name_plural = "Меню категорий"


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="имя", max_length=64, unique=True)
    description = models.TextField(verbose_name="описание", max_length=200, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"category with id - {self.pk}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="категория")
    name = models.CharField(verbose_name="имя продукта", max_length=128)
    image = models.ImageField(upload_to="product_images", blank=True, verbose_name="изображение")
    short_desc = models.CharField(verbose_name="краткое описание", max_length=100, blank=True)
    description = models.TextField(verbose_name="описание", max_length=200, blank=True)
    price = models.DecimalField(verbose_name="цена", max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name="количество товара на складе", default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"product with id - {self.pk}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"