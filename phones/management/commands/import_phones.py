import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from main import settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
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