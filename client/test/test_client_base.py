from django.test import TestCase
from client.models import ProductDB


class ProductDBTest(TestCase):
    def make_product(
        self,
        title='Product title',
        price=99.99,
        description='Product description',
        category='Product category'
    ):
        return ProductDB.objects.create(
            title=title,
            price=price,
            description=description,
            category=category
        )

    def test_str_method(self):
        product = self.make_product()
        self.assertEqual(str(product), 'Product title')
