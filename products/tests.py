from django.test import TestCase
from django.urls import reverse


class ProductListViewTest(TestCase):

    def test_should_return_200(self):
        url = reverse("products:list_products")  # ← nombre corregido
        response = self.client.get(url)
        breakpoint()
        self.assertEqual(response.status_code, 200)
