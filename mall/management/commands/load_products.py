"""
이 Django 관리 명령어는 GitHub에 호스팅된 JSON 파일에서 상품 데이터를 로드합니다. JSON 파일의 데이터를 기반으로 데이터베이스에 Category와 Product 모델을 생성하거나 업데이트합니다.

이 명령어는 다음 단계를 수행합니다:
1. 지정된 URL에서 상품 데이터 JSON 파일을 가져옵니다.
2. 상품 데이터를 순회하면서 해당하는 Category와 Product 모델을 생성하거나 업데이트합니다.
3. 각 상품에 대해 지정된 URL에서 상품 이미지를 다운로드하여 상품의 `photo` 필드에 저장합니다.

`Item` 데이터클래스는 JSON 파일의 상품 데이터를 표현하는데 사용됩니다.
"""

from dataclasses import dataclass

import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from tqdm import tqdm

from mall.models import Category, Product

BASE_URL = "https://raw.githubusercontent.com/pyhub-kr/dump-data/main/django-shopping-with-iamport/"


@dataclass
class Item:
    category_name: str
    name: str
    price: int
    priceUnit: str
    desc: str
    photo_path: str


class Command(BaseCommand):
    help = "Load products from JSON file."

    def handle(self, *args, **options):
        json_url = BASE_URL + "product-list.json"
        item_dict_list = requests.get(json_url).json()

        item_list = [Item(**item_dict) for item_dict in item_dict_list]
        category_name_set = {item.category_name for item in item_list}

        category_dict = {}
        for category_name in category_name_set:
            category, __ = Category.objects.get_or_create(
                name=category_name or "미분류"
            )
            category_dict[category.name] = category

        for item in tqdm(item_list):
            category: Category = category_dict[item.category_name or "미분류"]
            product, is_created = Product.objects.get_or_create(
                category=category,
                name=item.name,
                defaults={
                    "description": item.desc,
                    "price": item.price,
                },
            )
            if is_created:
                photo_url = BASE_URL + item.photo_path
                filename = photo_url.rsplit("/", 1)[-1]
                photo_data = requests.get(photo_url).content  # raw data
                product.photo.save(
                    name=filename,
                    content=ContentFile(photo_data),
                    save=True,
                )
