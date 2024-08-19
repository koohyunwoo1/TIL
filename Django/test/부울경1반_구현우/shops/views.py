from django.shortcuts import render, redirect
from .models import Product, Review
from .forms import ProductForm, ReviewForm


def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'shops/index.html', context)


def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('shops:detail', product.pk)
    
    else:
        form = ProductForm()
    
    context = {
        'form': form,
    }
    return render(request, 'shops/create.html', context)


def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    review_list = product.review_set.all()
    form = ReviewForm()
    context = {
        'product': product,
        'review_list': review_list,
        'form': form,
    }
    return render(request, 'shops/detail.html', context)


def update(request, product_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    product = Product.objects.get(pk=product_pk)
    if product.seller != request.user:
        return redirect('shops:detail', product_pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shops:detail', product.pk)
    
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'shops/update.html', context)


def delete(request, product_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    product = Product.objects.get(pk=product_pk)
    if product.seller != request.user:
        return redirect('shops:detail', product.pk)

    if request.method == 'POST':
        product.delete()
    
    return redirect('shops:index')


def create_review(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = request.user
            review.product = product
            review.save()
            return redirect('shops:detail', product.pk)
    
    review_list = product.review_set.all()
    context = {
        'form': form,
        'product': product,
        'review_list': review_list,
    }
    return render(request, 'shops/detail.html', context)


def delete_review(request, product_pk, review_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    review = Review.objects.get(pk=review_pk)
    if review.customer != request.user:
        return redirect('shops:detail', product_pk)
    
    
    if request.method == 'POST':
        review.delete()

    return redirect('shops:detail', product_pk)


# 문제 5. 상품 주문 처리 로직 오류 수정
def order(request, product_pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.method != 'POST':
        return redirect('shops:index')

    product = Product.objects.get(pk=product_pk)
    if product in request.user.order_list.all():
        request.user.order_list.remove(product)
    else:
        request.user.order_list.add(product)

    return redirect('shops:index')


# 문제 9. 총 금액 출력하는 부분 추가하기
def order_detail(request):
    order_list = request.user.order_list.all()

    context = {
        'order_list': order_list,
    }
    return render(request, 'shops/my_order.html', context)