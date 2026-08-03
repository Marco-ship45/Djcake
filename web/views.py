from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def contactos(request):
    return render(request,'contactos.html')


def noticias(request):
    return render(request,'noticias.html')


def pasteles(request):
    return render(request,'pasteles.html')


def enlaces(request):
    return render(request,'enlaces.html')