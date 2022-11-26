from rest_framework.test import APITestCase
from django.urls import reverse
from acoffe.models import coffe
from acoffe.serializers import CoffeSerializer
from rest_framework import status


class BookAPITestCase(APITestCase):
    def test_get_list(self):
        coffe_1 = coffe.objects.create(name='Test1', price=100)
        coffe_2 = coffe.objects.create(name='Test2', price=200.78, description='Test2')
        url = reverse('coffe-api')

        print(url)
        print(coffe_1)
        print(coffe_2)

        response = self.client.get(url)

        serial_data = CoffeSerializer([coffe_1, coffe_2], many=True).data
        serial_data = {'coffe': serial_data}

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serial_data, response.data)