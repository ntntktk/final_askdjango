from django.shortcuts import render
from .models import Category

def index(request):
    shop_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'shop_list': shop_list,
        })