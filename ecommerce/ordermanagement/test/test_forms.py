from django.test import TestCase
from ordermanagement.models import Product
from principal.models import  StateProduct

# Create your tests here.

# class ProductModelTest(TestCase):

#     @classmethod
#     def create_product(self, name="Producto1", quantity=4, unit_price = 4.5 ):
#         stateproduct = StateProduct.objects.create(name="En Stock",description="En Stock")
#         return Product.objects.create(name=name, quantity = quantity, unit_price= unit_price , state = stateproduct)
#         #Set up non-modified objects used by all test methods        

#     def test_product_creation(self):
#         p = self.create_product()
#         self.assertTrue(isinstance(p, Product))
#         # self.assertEqual(p.__unicode__(), p.name)