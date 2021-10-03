
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
import json
import os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        #fill ProductCategory
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        #fill Product
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            cat_name = product['category']
            product['category'] = ProductCategory.objects.get(name=cat_name)
            Product.objects.create(**product)

        #create superuser
        if not ShopUser.objects.filter(username='django'):
            ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=28)
