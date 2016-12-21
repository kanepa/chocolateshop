from django.test import TestCase
from django.shortcuts import render_to_response
from .models import Product

class ProductsModel(TestCase):


    def test_create_product(self):
        product = Product()
        product.name = "Single Hearts"
        product.description = "Our little handmade hearts are special."
        product.price = 1
        product.save()

        found = Product.objects.get(name="Single Hearts", price=1)
        self.assertEqual(found.description, "Our little handmade hearts are special.")
from django.test import TestCase

# Create your tests here.
