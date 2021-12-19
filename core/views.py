from django.shortcuts import render, redirect
from core.forms import CarrosForm
from core.models import Carros

def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, "view.html", data)

def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, "form.html", data)

def update(request, pk):
    return render(request, "index.html")