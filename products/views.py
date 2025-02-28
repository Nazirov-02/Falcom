
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from .models import Comment
from django.db.models import Q

from .models import Product
from .forms import CommentForm



# Create your views here.

def product_list(request):
    products = Product.objects.prefetch_related('images').all().order_by('-id')
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'products/product-list.html',{'page_obj': page_obj,'products':products})

def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    commentary = Comment.objects.filter(product=product)
    return render(request,'products/product-details.html',{'product':product, 'comments':commentary})



def comment(request,slug):
    products = Product.objects.get(slug=slug)
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            review = form.cleaned_data['review']
            rating = form.cleaned_data['rating']
            commentary = Comment.objects.create(
                name=name,
                email=email,
                review=review,
                product=products,
                rating=rating,
            )
            commentary.save()
            return redirect('products:comment',slug)
        print(form.errors)
    else:
        form = CommentForm()
    commentary = products.comments.all()
    context = {
        'comments': commentary,
        'form': form,
        'product': products,
    }
    return render(request, 'products/product-details.html', context)

def search(request):
    search = request.GET.get('q','')
    if search:
        products = Product.objects.filter(Q(category__title__icontains=search) | Q(name__icontains=search) ).all()
    else:
        products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/product-list.html', context)