from django.db import models

# Create your models here.

class Store(models.Model):
    """
    This model represents the stores that sell products.
    Variables:
    - name: The name of the store, maximum 255 characters.
    - rut: The rut of the store, maximum 255 characters.
    - address: The address of the store, maximum 255 characters.
    - start_at: The date and time when the store was created.
    - finish_at: The date and time the store stopped being a store. Can be null or blank.
    """
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField()

    def __str__(self):
        return self.name

class StoreEmail(models.Model):
    """
    This model represents the emails of a store.
    Variables:
    - email: The email of the store, maximum 255 characters.
    - is_active: The email is active or not.
    - store: The store that the email belongs to. This is null on delete.
    """
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.store.name + " - " + self.email

class StorePhone(models.Model):
    """
    This model represents the phones of a store.
    Variables:
    - phone: The phone of the store, maximum 255 characters.
    - is_active: The phone is active or not.
    - store: The store that the phone belongs to. This is null on delete.
    """
    phone = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.store.name + " - " + self.phone
