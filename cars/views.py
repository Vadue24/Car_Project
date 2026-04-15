from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .models import Car
from .forms import CarForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from .serializer import ArticleSerializer

from django.core.paginator import Paginator


def cars_home(request):
    sort_param = request.GET.get('sort', '')
    search_query = request.GET.get('search', '')
    cars = Car.objects.all()

    if sort_param == 'lowtohigh':
        cars = cars.order_by('price')
    elif sort_param == 'hightolow':
        cars = cars.order_by('-price')
    elif sort_param == 'atoz':
        cars = cars.order_by('title')
    elif sort_param == 'ztoa':
        cars = cars.order_by('-title')
    else:
        cars = cars.order_by('-date')

    if search_query:
        cars = cars.filter(title__icontains=search_query)

    paginator = Paginator(cars, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    return render(request, 'cars/cars_home.html', {
        'page_obj': page_obj,
        'sort_param': sort_param,
        'search_query': search_query,
    })


class CarsUpdateView(UpdateView):
    model = Car
    template_name = 'cars/create.html'

    form_class = CarForm
    success_url = '/cars/'


class CarsDeleteView(DeleteView):
    model = Car
    template_name = 'cars/cars_delete.html'
    success_url = '/cars/'


class CarsDetailView(DetailView):
    model = Car
    template_name = 'cars/cars_detail.html'
    context_object_name = 'post'


def handle_uploads(f):
    with open(f'media/car_images/{f.name}', 'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)


def create(request):
    error = ''
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            handle_uploads(form.cleaned_data['picture'])
            return redirect('cars_home')
        else:
            error = 'INVALID FORM!'
            print('error')

    form = CarForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'cars/create.html', data)


# --------------API--------------------

class ArticleApi(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get']
    renderer_classes = [JSONRenderer]
