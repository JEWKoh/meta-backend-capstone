from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from restaurant.models import Booking

class BookingViewSetTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.booking1 = Booking.objects.create(
            name='John Doe',
            number_of_guests=2,
            booking_date='2024-07-01',
            reservation_slot=1
        )
        self.booking2 = Booking.objects.create(
            name='Jane Doe',
            number_of_guests=4,
            booking_date='2024-07-02',
            reservation_slot=2
        )

        self.valid_payload = {
            'name': 'Alice Smith',
            'number_of_guests': 3,
            'booking_date': '2024-07-03',
            'reservation_slot': 3
        }
        self.invalid_payload = {
            'name': '',
            'number_of_guests': -1,
            'booking_date': 'invalid-date',
            'reservation_slot': -1
        }

    def test_get_all_bookings(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_valid_booking(self):
        response = self.client.post(reverse('booking-list'), data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 3)

    def test_create_invalid_booking(self):
        response = self.client.post(reverse('booking-list'), data=self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_booking(self):
        response = self.client.get(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.booking1.name)

    def test_update_booking(self):
        update_payload = {
            'name': 'John Smith',
            'number_of_guests': 5,
            'booking_date': '2024-07-05',
            'reservation_slot': 4
        }
        response = self.client.put(reverse('booking-detail', kwargs={'pk': self.booking1.pk}), data=update_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking1.refresh_from_db()
        self.assertEqual(self.booking1.name, 'John Smith')

    def test_delete_booking(self):
        response = self.client.delete(reverse('booking-detail', kwargs={'pk': self.booking1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 1)
