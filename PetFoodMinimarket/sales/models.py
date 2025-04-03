from django.db import models
from products.models import Product
from stores.models import Store
# Create your models here.

# Sale model
class Sale(models.Model):
    """
    This model represents the sales that are made in the store.
    Variables:
    - total_price: The total price of the sale.
    - total_iva: The total iva of the sale.
    - start_at: The date and time when the sale was created.
    - store: The store that the sale belongs to. This is null on delete.
    - user: The user that made the sale. This is null on delete.
    """
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_iva = models.DecimalField(max_digits=12, decimal_places=2)
    start_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('users.MinimarketUser', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.store.name + " - " + str(self.start_at) + " - " + self.user.username

# Sale detail model
class SaleDetail(models.Model):
    """
    This model represents the details of a sale.
    Variables:
    - quantity: The quantity of the product sold.
    - unit_price_with_iva: The unit price of the product with IVA.
    - unit_iva: The unit IVA of the product.
    - total_price: The total price of the product.
    - total_iva: The total IVA of the product.
    - sale: The sale that the detail belongs to. This is null on delete.
    - product: The product that was sold. This is null on delete.
    """
    quantity = models.PositiveIntegerField()
    unit_price_with_iva = models.DecimalField(max_digits=12, decimal_places=2)
    unit_iva = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_iva = models.DecimalField(max_digits=12, decimal_places=2)
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.pk) + " - " + self.product.name