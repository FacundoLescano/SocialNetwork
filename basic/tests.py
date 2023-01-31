from django.test import TestCase
from django.urls.base import reverse


# Create your tests here.

class TestIndexViews(TestCase):

    def test_status_response_index(self):
        """ return the status code 200 to check everything is correct """
        response = self.client.get(reverse("basic:index"))
        self.assertIs(response.status_code, 200)