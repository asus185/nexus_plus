from .models import Product
from category.models import *
from product.models import *
from django.db.models import Prefetch,Count
from django.core.paginator import Paginator
from .models import *
from  user.models import User
from django.shortcuts import redirect, render





def product_list(request):
    page = request.GET.get('page', 1)
    products = Product.objects.prefetch_related(
        Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True),
                 to_attr='main_image'))
    paginator= Paginator(products, 2)
    page_obj=paginator.get_page(page)
    reg = Region.objects.all()
    categories = Category.objects.all()
    ctx = {
        "products": products,
        "page_obj": page_obj,
        "count": paginator.count,
        "reg": reg,
        "categories": categories,
        "product": None,

    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    product = Product.objects.prefetch_related(
        Prefetch(
            'images',
            queryset=ProductImage.objects.all(),
            to_attr='main_images'
        )
    ).get(pk=pk)

    ctx = {
        "product": product,
    }
    return render(request, 'detail.html', ctx)


def product_create(request):
    categories = Category.objects.all()
    regions = Region.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        category = request.POST.get('category')
        brand = request.POST.get('brend')
        condition = request.POST.get('condition')
        status = request.POST.get('status')
        price = request.POST.get('price')
        price_on_call = request.POST.get('price_on_call')

        product = Product.objects.create(

            title=title,
            description=description,
            location_id=location,
            category_id=category,
            brend_id=brand,
            condition=condition,
            status=status,
            price=price,
            price_on_call=price_on_call,
            user=request.user

        )

        for image in request.FILES.getlist('images'):
            ProductImage.objects.create(product=product, image=image)
        return redirect('/products/')

    ctx = {

        "categories": categories,
        "regions": regions,

    }

    return render(request, 'product_create.html', ctx)
