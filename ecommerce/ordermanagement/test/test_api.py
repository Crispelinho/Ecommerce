from ordermanagement.models import Product, Order
from ordermanagement import views
from django.urls import reverse
from rest_framework import status
from principal.models import  StateProduct
from rest_framework.test import APITestCase

# Create your tests here.

class OrderAPITest(APITestCase):

    def test_create_order(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("ordermanagement:order__add")
        # url = '/ordermanagement/order/'
        print(url)
        data =     {
                    "orderproduct_set": [
                            {
                                "quantity": 3.0,
                                "product": 1,
                                "order": 1
                            },
                            {
                                "quantity": 4.0,
                                "product": 2,
                                "order": 1
                            }
                        ],
                        "shipment_address": "Carrera 17 # 45 - 66",
                        "amount": 45.0,
                        "state": 1,
                        "payment_method": 1,
                        "user": 1
                    }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
