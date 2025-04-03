from django.db import models
from django.contrib.auth.models import AbstractUser
from stores.models import Store
# Create your models here.

class MinimarketUser(AbstractUser):
    """
    This model represents the users of the system.
    Django variables:
    - password: The password of the user.
    - last_login: The last time the user logged in.
    - is_superuser: The user is a superuser or not.
    - username: The username of the user.
    - last_name: The last name of the user.
    - email: The email of the user.
    - is_staff: The user is a staff member or not.
    - is_active: The user is active or not.
    - date_joined: The date and time when the user was created.
    - first_name: The first name of the user.
    Custom variables:
    - date_of_birth: The date of birth of the user.
    - phone: The phone number of the user, maximum 255 characters.
    - address: The address of the user, maximum 255 characters.
    - rut: The rut of the user, maximum 255 characters.
    - profile_picture: The profile picture of the user, uploaded to 'profile_pictures/'.
    - store: The store that the user belongs to. This is null on delete.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    rut = models.CharField(max_length=255, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username