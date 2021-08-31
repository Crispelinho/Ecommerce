from ordermanagement.models import Product, Order
from ordermanagement.serializers import *
from ordermanagement.models import *
from django.urls import reverse
from rest_framework import status
from principal.models import  StateProduct
from rest_framework.test import APITestCase
import json
from django.test import TestCase
from django.conf import settings
import os
# Create your tests here.


class ProductTest(TestCase):
    """ Test module for GET all puppies API """
    def setUp(self):
        state=StateProduct.objects.create(name="En Stock", description="En Stock")
        print(state)
        Product.objects.create(
            name='Producto1', quantity=3.0, unit_price=3.0, state=state)
        Product.objects.create(
            name='Producto2', quantity=4.0, unit_price=4.0, state=state)
        Product.objects.create(
            name='Producto3', quantity=5.0, unit_price=6.0, state=state)
        Product.objects.create(
            name='Producto4', quantity=6.0, unit_price=7.0, state=state)

    def test_get_all_puppies(self):
        # get API response
        response = self.client.get(reverse('products-list'))
        # get data from db
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class ProductTest(APITestCase):
#     # fixtures = ['orders']
#     url = reverse('products-list')
#     print(url)
#     path = os.path.join(settings.PROJECT_DIR, 'fixtures','product.json')
#     with open(path) as file:
#         data = json.load(file)

#     def test_create_order(self):
#         """
#         Ensure we can create a new account object.
#         """
#         print(self.url)
#         print("XXXXXXXXXXXXXXXXXXXXXX")
#         print(self.data)
#         print("XXXXXXXXXXXXXXXXXXXXXX")

#         response = self.client.post(self.url, self.data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class OrderAPITest(APITestCase):
#     fixtures = ['orders']
#     url = reverse('orders-list')
#     def test_create_order(self):
#         """
#         Ensure we can create a new account object.
#         """
#         print(self.data)
#         print("XXXXXXXX")
#         response = self.client.post(self.url, self.data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Order.objects.count(), 1)

#     def test_retrieve_order(self):
#         order = Order.objects.first()
#         response = self.client.get(f'/ordermanagement/order/{order.id}')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         response_json = response.json()


