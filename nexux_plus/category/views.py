from django.shortcuts import render, redirect
from flask import ctx

from .forms import RegionForm
from .models import Region

def region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        print(request.POST)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            form.save()
            return redirect('region')
    else:
        form = RegionForm()

    ctx = {
            'form': form
    }
    return render(request,'region.html', ctx)


def contact_view(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('region')

    else:
        form = RegionForm()
    ctx = {
        'form': form,
    }
    return render(request, 'region.html', ctx)
