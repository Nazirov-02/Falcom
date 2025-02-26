
from django.core.paginator import Paginator
from django.db.models import Avg
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from .models import Comment
from django.db.models import Q

from .models import Product
from .forms import CommentForm



# Create your views here.

def product_list(request):
    products = Product.objects.prefetch_related('images').all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'products/product-list.html',{'page_obj': page_obj})

def product_detail(request,pk):
    products = Product.objects.prefetch_related('images').get(id=pk)
    commentary = Comment.objects.filter(product=products)
    return render(request,'products/product-details.html',{'products':products, 'comments':commentary})



def comment(request,pk):
    products = Product.objects.get(id=pk)
    if request.method == 'POST':
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
            return redirect('comment-detail',pk=pk)
        print(form.errors)
    else:
        form = CommentForm()
    commentary = Comment.objects.filter(id=pk)

    context = {
        'comments': commentary,
        'form': form,
        'products': products,
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