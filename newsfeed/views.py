from django.shortcuts import render, redirect
from .models import Product
from .forms import PostProductForm
from django.contrib import messages

def newsfeed(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'newsfeed.html', {'products': products})

def post_product(request):
    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Your product has been successfully listed!')
            return redirect('newsfeed')
    else:
        form = PostProductForm()
    return render(request, 'post_product.html', {'form': form})

