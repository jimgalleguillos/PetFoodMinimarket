from django.db import models
from stores.models import Store
# Create your models here.

# Category model
class Category(models.Model):
    """
    This model represents the categories that a product could belong to.
    Variables:
    - name: The name of the category, maximum 255 characters.
    - start_at: The date and time when the category was created.
    - finish_at: The date and time the category stopped being used. Can be null or blank.
    - parent_category: The parent category of the category. This is null on delete and can be null or blank.
    """
    name = models.CharField(max_length=255)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    """
    This model represents the products that are sold in the store.
    Variables:
    - name: The name of the product, maximum 255 characters.
    - bar_code: The bar code of the product, maximum 255 characters. This is unique and can be null or blank.
    - description: The description of the product.
    - is_bulk: The product is bulk or not.
    - start_at: The date and time when the product was created.
    - finish_at: The date and time when the product was finished or changed. Can be null or blank.
    - store: The store that the product belongs to. This is null on delete.
    - unit_of_measure: The unit of measure of the product. This is null on delete.
    """
    name = models.CharField(max_length=255)
    bar_code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    is_bulk = models.BooleanField(default=False)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    store = models.ForeignKey(Store,on_delete=models.SET_NULL, null=True)
    unit_of_measure = models.ForeignKey('ProductMeasure', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
    
class ProductMeasure(models.Model):
    """
    This model represents the measures of a product.
    Variables:
    - unit_of_measure: The unit of measure of the product, maximum 50 characters.
    """
    unit_of_measure = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.unit_of_measure

# Product image model
class ProductImage(models.Model):
    """
    This model represents the images of a product.
    Variables:
    - image: The image of the product. This is an image field that uploads to the 'products/' directory.
    - is_primary: The image is the primary image or not.
    - product: The product that the image belongs to. This is null on delete.
    """
    image = models.ImageField(upload_to='products/')
    is_primary = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product.name
    
# Product stock model
class ProductStockHistory(models.Model):
    """
    This model represents the stock of a product.
    Variables:
    - quantity: The quantity of the product in stock.
    - start_at: The date and time when the stock was created.
    - finish_at: The date and time when the stock was finished or changed. Can be null or blank.
    - product: The product that the stock belongs to. This is null on delete.
    - reason: The reason for the stock change. This is null on delete.
    """
    quantity = models.PositiveIntegerField()
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    reason = models.ForeignKey('StockReason', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product.name
    
# Stock Reason model
class StockReason(models.Model):
    """
    This model represents the reasons for the stock change.
    Variables:
    - reason: The name of the reason, maximum 255 characters.
    """
    reason = models.CharField(max_length=255)
    def __str__(self):
        return self.reason

# Product pricing model
class ProductPriceHistory(models.Model):
    """
    This model represents the prices of a product.
    Variables:
    - unit_price_without_iva: The price of the product without IVA.
    - unit_price_with_iva: The price of the product with IVA.
    - start_at: The date and time when the price was created.
    - finish_at: The date and time when the price was finished or changed. Can be null or blank.
    - product: The product that the price belongs to. This is null on delete.
    """
    unit_price_without_iva = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price_with_iva = models.DecimalField(max_digits=12, decimal_places=2)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name

# Product category model
class productCategory(models.Model):
    """
    This model represents the categories that a product belongs to.
    Variables:
    - product: The product that the category belongs to. This is null on delete.
    - category: The category that the product belongs to. This is null on delete.
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.product.name} - {self.category.name}"