from django.test import TestCase
from django.urls import reverse


class MiOrdenViewtest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("orders:my_orders")
        response = self.client.get(url)
        self.assertEqual(response.url, "/accounts/login/?next=/orders/my-orders/")
