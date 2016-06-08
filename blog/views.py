from django.shortcuts import render, get_object_or_404
from .models import Category, Shop, Review

def index(request):
    shop_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'shop_list': shop_list,
        })

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category.html', {
        'category': category,
        })

def category_new(request, category_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Category, pk=category_pk)
            comment.user = request.user
            comment.save()
            messages.success(request, '새로운 카테고리가 생성되었습니다.')
            return redirect('blog:category_detail', category_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/category.html')

    def category_edit(request, category_pk, pk):
        comment = get_object_or_404(Category, pk=pk)

        if request.method == 'POST':
            form = CommentForm(request,POST, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = get_object_or_404(Category, pk=category_pk)
                comment.user = request.user
                comment.save()
                messages.success(request, '새로운 카테고리가 생성되었습니다.')