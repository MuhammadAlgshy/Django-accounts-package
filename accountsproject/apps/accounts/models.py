from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

class AbstractAuditModel(models.Model):
    # A timestamp representing when this object was created.
    createdDate = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updatedDate = models.DateTimeField(auto_now=True)

    # A field to know who updated the record.
    updatedBy =  models.CharField(max_length=200, null=True, blank=True)

    # A field to know who created the record.
    createdBy = models.CharField(max_length=200, default="System")

    # A field to know who deleted the record.
    deletedBy =  models.CharField(max_length=200, null=True, blank=True)

    # A timestamp reprensenting when this object was deleted.
    deletedDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        # ordering = ["-date_created", "-date_updated"]


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a `User` with an email and password.
        """
        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and return a `User` with superuser powers.
        """
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, AbstractAuditModel):
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS=[]
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        if not self.first_name:
            return self.email
        return self.first_name
