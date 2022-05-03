from django.shortcuts import render, redirect
import csv
from phones.models import Phone
from main import settings


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

def import_csv(request):
    template = 'base.html'
    context = {}

    with open(settings.PHONES, 'r') as csvfile:
        phone_reader = csv.reader(csvfile, delimiter=';')
        # пропускаем заголовок
        next(phone_reader)

        # TODO: Добавьте сохранение модели
        for line in phone_reader:
            new_phone = Phone(
                name=line[1],
                price=int(line[3]),
                image=line[2],
                release_date=line[4],
                lte_exists=line[5],
                slug=''
            )
            new_phone.get_slug()
            new_phone.save()
    return render(request, template, context)

