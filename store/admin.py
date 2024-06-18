from django.contrib import admin
from .models import Product, Category, ProductPrice


class ProductPriceInline(admin.TabularInline):
    """
    this is the class that we declared for adding field's of the product price into the Product admin page
    """
    model = ProductPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_price')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [ProductPriceInline,]
    fieldsets = [
        (
            "Main",
            {
                'fields': ('name', 'category', 'description')
            }
        ),
        (
            "Detail",
            {
                'classes': ('collapse',),
                'fields': ('serial_number', 'image'),
            }
        )
    ]

    def get_price(self, obj):
        """
        this function is for retriving the price of the product
        """
        try:
            product_price = obj.productprice_set.first()
            return product_price.price
        except (AttributeError, TypeError, ProductPrice.DoesNotExist):
            return "N/A"

    get_price.short_description = 'Price'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    this class for handling and showing the categories inside the admin page
    """
    list_display = ('name', 'parent')
