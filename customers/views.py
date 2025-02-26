from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerForm
from .models import Customers
# Create your views here.
def customers_list(request):
    customers = Customers.objects.all()
    return render(request,'ecomerce/customers.html',{'customers':customers})

def customer_detail(request,pk):
    customer = Customers.objects.get(pk=pk)
    return render(request,'ecomerce/customer-details.html',{'customer':customer})

def delete_customer(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customers')
    return render(request, 'ecomerce/delete_customer.html',{'customer':customer})

def edit_customer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == "POST":

        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'ecomerce/edit_customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()

    context = {
        'form': form,
    }
    return render(request, 'ecomerce/add_customer.html', context)
