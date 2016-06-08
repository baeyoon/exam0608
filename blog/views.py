from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
from .models import Shop

# Create your views here.

def index(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {
        'category_list': category_list,
        })

def category_detail(request, pk):
    shop_list = Shop.objects.all()
    return render(request, 'blog/category_detail.html', {
        'shop_list' : shop_list,
        })

def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
             category = form.save()
             return redirect('blog:category_list', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'blog/category_new.html', {'form' : form})

def shop_detail(request, pk):
    shop = Shop.objects.get(pk=category_pk)
    return render(request, 'blog/shop_detail.html', {'shop' : shop})

#def category_edit(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
             category = form.save()
             return redirect('blog:category_list', category.pk)
    else:
        form = CategoryForm()
    return render(request, 'blog/category_new.html', {'form' : form})