from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Menu

class MenuViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.menu_item1 = Menu.objects.create(
            title='Pizza',
            price=12.99,
            description='Delicious cheese pizza',
            inventory=10
        )
        self.menu_item2 = Menu.objects.create(
            title='Burger',
            price=8.99,
            description='Juicy beef burger',
            inventory=5
        )

        self.valid_payload = {
            'title': 'Pasta',
            'price': 15.99,
            'description': 'Creamy Alfredo pasta',
            'inventory': 7
        }
        self.invalid_payload = {
            'title': '',
            'price': -1.00,
            'description': '',
            'inventory': -5
        }

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_valid_menu_item(self):
        response = self.client.post(reverse('menu-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)

    def test_create_invalid_menu_item(self):
        response = self.client.post(reverse('menu-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_menu_item(self):
        response = self.client.get(reverse('menu-detail', kwargs={'pk': self.menu_item1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.menu_item1.title)

    def test_update_menu_item(self):
        update_payload = {
            'title': 'Updated Pizza',
            'price': 14.99,
            'description': 'Updated delicious cheese pizza',
            'inventory': 15
        }
        response = self.client.put(reverse('menu-detail', kwargs={'pk': self.menu_item1.pk}), data=update_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item1.refresh_from_db()
        self.assertEqual(self.menu_item1.title, 'Updated Pizza')

    def test_delete_menu_item(self):
        response = self.client.delete(reverse('menu-detail', kwargs={'pk': self.menu_item1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)
