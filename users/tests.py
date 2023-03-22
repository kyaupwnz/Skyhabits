from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


# Create your tests here.

class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='manager@test.ru', city='Tomsk', is_staff=True, is_active=True)
        self.user.set_password('manager')
        self.user.save()
        response = self.client.post('/users/api/token/', {"email": 'manager@test.ru',
                                                          "password": "manager"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_user(self):
        response = self.client.post('/users/', {'email': 'manager2@test.ru', 'password': 'manager', 'city': 'Tomsk'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_user(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{'email': 'manager@test.ru', 'city': 'Tomsk', 'chat_id': None}])

    def test_update_user(self):
        response = self.client.put('/users/1/', {'email': 'manager@test.ru',
                                                 'chat_id': '1111111111',
                                                 'city': 'Moscow'
                                                 }
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
                {
                    'email': 'manager@test.ru',
                    'chat_id': '1111111111',
                    'city': 'Moscow'
                }
        )

    def test_detail_user(self):
        response = self.client.get('/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'email': 'manager@test.ru',
                'chat_id': None,
                'city': 'Tomsk'
            }
        )

    def test_delete_user(self):
        response = self.client.delete('/users/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TelegramTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='manager@test.ru', city='Tomsk', is_staff=True, is_active=True)
        self.user.set_password('manager')
        self.user.save()
        response = self.client.post('/users/api/token/', {"email": 'manager@test.ru',
                                                          "password": "manager"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_Telegram(self):
        response = self.client.get('/users/telegram/')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "url": "t.me/Kyau_habits_bot",
            }
        )
