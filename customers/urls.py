from django.urls import path
from customers.views import customer_detail, customers_list, delete_customer, edit_customer, add_customer, export_data

app_name = 'customers'

urlpatterns = [

path('customers/',customers_list, name='customers'),
path('customer_detail/<slug:slug>/',customer_detail, name='customer_detail'),
path('delete_customer/<slug:slug>/',delete_customer, name='delete_customer'),
path('edit_customer/<slug:slug>/',edit_customer, name='edit_customer'),
path('customer_add/',add_customer, name='add_customer'),
path('data_format/',export_data,name='data_format'),
]