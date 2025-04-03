from django.db import models
from products.models import Product
from stores.models import Store
# Create your models here.

# Supplier model
class Supplier(models.Model):
    """"
    This model represents the suppliers that supply products to the store.
    Variables:
    - name: The name of the supplier, maximum 255 characters.
    - rut: The rut of the supplier, maximum 255 characters.
    - start_at: The date and time when the supplier was created.
    - finish_at: The date and time when the supplier stopped being a supplier. Can be null or blank.
    - store: The store that the supplier belongs to. This is null on delete.
    """
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

# Supplier address model
class SupplierAddress(models.Model):
    """
    This model represents the addresses of a supplier.
    Variables:
    - address: The address of the supplier, maximum 255 characters.
    - is_active: The address is active or not.
    - supplier: The supplier that the address belongs to. This is null on delete.
    """
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.supplier.name + " - " + self.address

# Supplier email model
class SupplierEmail(models.Model):
    """
    This model represents the emails of a supplier.
    Variables:
    - email: The email of the supplier, maximum 255 characters.
    - is_active: The email is active or not.
    - supplier: The supplier that the email belongs to. This is null on delete.
    """
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.supplier.name + " - " + self.email

# Supplier phone model
class SupplierPhone(models.Model):
    """
    This model represents the phones of a supplier.
    Variables:
    - phone: The phone of the supplier, maximum 255 characters.
    - is_active: The phone is active or not.
    - supplier: The supplier that the phone belongs to. This is null on delete.
    """
    phone = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.supplier.name + " - " + self.phone

# Supplier product model
class SupplierProduct(models.Model):
    """
    This model represents the products that a supplier supplies to the store.
    Variables:
    - product: The product that the supplier supplies. This is null on delete.
    - is_active: The product is active or not.
    - supplier: The supplier that supplies the product. This is null on delete.
    """
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.supplier.name + " - " + self.product.name

# Supplier product price history model
class SupplierProductPriceHistory(models.Model):
    """
    This model represents the price history of a product supplied by a supplier.
    Variables:
    - unit_price_without_iva: The unit price of the product without IVA.
    - unit_price_with_iva: The unit price of the product with IVA.
    - start_at: The date and time when the price was created.
    - finish_at: The date and time when the price was finished or changed. Can be null or blank.
    - supplier_product: The supplier product that the price belongs to. This is null on delete.
    """
    unit_price_without_iva = models.DecimalField(max_digits=12, decimal_places=2)
    unit_price_with_iva = models.DecimalField(max_digits=12, decimal_places=2)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)
    supplier_product = models.ForeignKey(SupplierProduct, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.supplier_product.product.name + " - " +  self.supplier_product.supplier.name 