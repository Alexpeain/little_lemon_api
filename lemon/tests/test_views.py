from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from littlelemonapi.models import MenuItem
from littlelemonapi.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name="Lemonade Dart")
        self.menu2 = MenuItem.objects.create(name="Fresh Python soup")
        self.menu3 = MenuItem.objects.create(name="Java Latte")

    def test_getall(self):
        url = reverse("menu-items")
        response = self.client.get(url)
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)