from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product
from .models import Customers
from django.contrib import messages
from .forms import CustomerForm
from .models import Customers
# Create your views here.
import json
import csv
def customers_list(request):
    customers = Customers.objects.all()
    return render(request,'customers/customers.html',{'customers':customers})

def customer_detail(request,slug):
    customer = Customers.objects.get(slug=slug)
    return render(request,'customers/customer-details.html',{'customer':customer})

def delete_customer(request, slug):
    customer = get_object_or_404(Customers, slug=slug)
    if request.method == "POST":
        customer.delete()
        return redirect('customers:customers')
    return render(request, 'customers/delete_customer.html',{'customer':customer})

def edit_customer(request, slug):
    customer = Customers.objects.get(slug=slug)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customers')
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'customers/edit_customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if Customers.objects.filter(phone=phone).exists():
                messages.error(request, 'This phone already used')
                return redirect('customers:add_customer')
            form.save()
            return redirect('customers:customers')
    else:
        form = CustomerForm()

    context = {
        'form': form,
    }
    return render(request, 'customers/add_customer.html', context)



def default_slugs_for_base(request):
    product_slugs = Product.objects.values_list('slug', flat=True)
    product_slug = product_slugs[0] if product_slugs else None

    customers_slugs = Customers.objects.values_list('slug', flat=True)
    customers_slug = product_slugs[0] if customers_slugs else None
    return render(request,'base.html',{'product_slug':product_slug,'customers_slug':customers_slug})





def export_data(request):
    format = request.GET.get('format', '')
    response = None
    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=customer_list.csv'
        writer = csv.writer(response)
        writer.writerow(['Id', 'Full Name', 'Email', 'Phone Number', 'Address'])
        for customer in Customers.objects.all():
            writer.writerow([customer.id, customer.name, customer.email, customer.phone, customer.address])
    elif format == 'json':
        response = HttpResponse(content_type='application/json')
        data = list(Customers.objects.all().values('full_name', 'email', 'address', 'phone_number'))
        for customer in data:
            customer['phone_number'] = str(customer['phone_number'])
        response.write(json.dumps(data, indent=3))
        response['Content-Disposition'] = 'attachment; filename=customers.json'
    elif format == 'xlsx':
        pass
    else:
        response = HttpResponse(status=404)
        response.content = 'Bad request'

    return response


