from django.shortcuts import render, get_object_or_404
from .models import Category, Shop, Review

def index(request):
    shop_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'shop_list': shop_list,
        })

def category_new(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category.html', {
        'category': category,
        })