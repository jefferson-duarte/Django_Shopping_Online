from django.test import TestCase, Client
from django.urls import reverse
from .test_client_base import ProductDBTest


class HomeViewTest(TestCase):

    def test_if_home_view_returns_200(self):
        client = Client()

        response = client.get(reverse('products:home'))
        self.assertEqual(response.status_code, 200)

    def test_if_home_view_returns_correct_template(self):
        client = Client()

        response = client.get(reverse('products:home'))
        self.assertTemplateUsed(response, 'client/pages/home.html')


class ProductDetailViewTest(TestCase):
    def test_if_product_detail_view_returns_200(self):
        client = Client()
        response = client.get(reverse('products:product_detail', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_if_product_detail_view_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('products:product_detail', args=[1]))
        self.assertTemplateUsed(response, 'client/pages/product_detail.html')


class ElectronicsViewTest(TestCase):
    def test_if_electronics_view_returns_200(self):
        client = Client()
        response = client.get(reverse('products:electronics'))
        self.assertEqual(response.status_code, 200)

    def test_if_electronics_view_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('products:electronics'))
        self.assertTemplateUsed(response, 'client/pages/electronics.html')


class JeweleryViewTest(TestCase):
    def test_if_jewelery_view_returns_200(self):
        client = Client()
        response = client.get(reverse('products:jeweleries'))
        self.assertEqual(response.status_code, 200)

    def test_if_jewelery_view_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('products:jeweleries'))
        self.assertTemplateUsed(response, 'client/pages/jewelery.html')


class MenClothingViewTest(TestCase):
    def test_if_men_clothing_view_returns_200(self):
        client = Client()
        response = client.get(reverse('products:men_clothing'))
        self.assertEqual(response.status_code, 200)

    def test_if_men_clothing_view_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('products:men_clothing'))
        self.assertTemplateUsed(response, 'client/pages/men_clothing.html')


class WomenClothingViewTest(TestCase):
    def test_if_women_clothing_view_returns_200(self):
        client = Client()
        response = client.get(reverse('products:women_clothing'))
        self.assertEqual(response.status_code, 200)

    def test_if_women_clothing_view_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('products:women_clothing'))
        self.assertTemplateUsed(response, 'client/pages/women_clothing.html')


class ProductCartTest(ProductDBTest):
    def test_if_product_cart_view_returns_302(self):
        client = Client()

        response = client.get(
            reverse('products:product_cart', args=[1]))
        self.assertEqual(response.status_code, 302)
