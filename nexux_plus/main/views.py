from django.db.models import Prefetch
from django.shortcuts import render
from category.models import Category,Region
from product.models import Product, ProductImage
from .forms import EmailForm
from django.core.mail import send_mail

def main(request):
    categories = Category.objects.filter(is_main=True)
    products = Product.objects.prefetch_related(
        Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True),
                 to_attr='main_image')
    )
    reg = Region.objects.all()

    ctx={
        "categories":categories,
        "products":products,
        "a" : 1234567890,
        "reg" : reg

    }
    return render(request, "index.html",ctx)

def contact(request):
    form = EmailForm()
    send_mail(
        'Subject here',
        'Here is the message.',
        'nurullostepn3@gmail.com',
        ['obidzeromax@gmail.com'],
        fail_silently=False,
    )
    print('END.....')
    ctx = {
        "form": form
    }
    return render(request, 'contact.html', ctx)





