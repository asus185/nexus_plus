from django.shortcuts import render


def login(request):
    ctx = {

    }
    return render(request,'login.html',ctx)

def register(request):
    ctx = {
        
    }
    return render(request,'register.html', ctx)


