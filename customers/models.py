from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customers(BaseModel):
    img = models.ImageField(upload_to='img', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField(region='UZ')
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    vat_number = models.PositiveIntegerField(null=True, blank=True)
    invoice_prefix = models.CharField(max_length=35,null=True, blank=True)


    def __str__(self):
        return self.name