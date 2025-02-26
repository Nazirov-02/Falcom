from django import forms

from customers.models import Customers


class CustomerForm(forms.ModelForm):
    class Meta:
      model = Customers
      fields = '__all__'
