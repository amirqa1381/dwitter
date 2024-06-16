from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    """
    this model is used to store categories
    """
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    this model is used to store products
    """
    name = models.CharField(max_length=150, verbose_name='Name')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    serial_number = models.PositiveIntegerField(verbose_name='Serial Number')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category', related_name='product')
    image = models.ImageField(upload_to='products', verbose_name='Image')

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    """
    this model is used to store product prices
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    price = models.PositiveIntegerField(verbose_name='Price')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Seller')

    def __str__(self):
        return f"{self.seller.username} / {self.price}"

