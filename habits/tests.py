from datetime import datetime

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


# Create your tests here.


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User(email='manager@test.ru', city='Tomsk', is_staff=True, is_active=True)
        self.user.set_password('manager')
        self.user.save()
        response = self.client.post('/users/api/token/', {"email": 'manager@test.ru',
                                               "password": "manager"})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.current_time = datetime.now().strftime('%H:%M:%S')
        self.test_data = {
            'place': 'Дома',
            'time': self.current_time,
            'action': 'Мыть посуду',
            'is_pleasant': False,
            'related_habit': '',
            'periodicity': 1,
            'reward': 'Шоколадка',
            'execution_time': 60,
            'is_public': True
        }
        self.response_test_data = {
            'id': 1,
            'place': 'Дома',
            'time': self.current_time,
            'action': 'Мыть посуду',
            'is_pleasant': False,
            'related_habit': None,
            'periodicity': 1,
            'reward': 'Шоколадка',
            'execution_time': 60,
            'is_public': True,
            'last_time_executed': None
        }

    def test_habit_create(self):
        response = self.client.post('/habits/', self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), self.response_test_data)

    def test_habit_list(self):
        self.test_habit_create()
        response = self.client.get('/habits/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [self.response_test_data])

    def test_habit_detail(self):
        self.test_habit_create()
        response = self.client.get('/habits/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), self.response_test_data)

    def test_habit_delete(self):
        self.test_habit_create()
        response = self.client.delete('/habits/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_update(self):
        self.test_habit_create()
        response = self.client.put('/habits/1/', {
            'place': 'На улице',
            'time': self.current_time,
            'action': 'Сделать зарядку',
            'is_pleasant': False,
            'related_habit': '',
            'periodicity': 2,
            'execution_time': 120,
            'reward': 'Выпить чашку кофе',
            'is_public': False
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'place': 'На улице',
                'time': self.current_time,
                'action': 'Сделать зарядку',
                'is_pleasant': False,
                'related_habit': None,
                'periodicity': 2,
                'execution_time': 120,
                'reward': 'Выпить чашку кофе',
                'is_public': False,
                'last_time_executed': None
            }
        )