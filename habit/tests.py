from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User


class HabitAPITest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='user@example.com', password='test')
        self.group = Group.objects.create(name='manager')
        self.group.user_set.add(self.user)
        self.client.force_authenticate(user=self.user)  # Аутентифицируем клиента с созданным пользователем

    def test_habit(self):
        # create habit
        data = {
            "name": "test habit 1",
            "place": "my room",
            "time": "23:42",
            "action": "squats",
            "is_nice": False,
            # "related": 0,
            "period": 1,
            # "reward": "string",
            "time_to_complete": 110,
            "is_public": True
        }
        response = self.client.post('/habit/create-habit/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # list all habit
        response = self.client.get('/habit/all-habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # list my habit
        response = self.client.get('/habit/my-habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # get habit
        response = self.client.get('/habit/get-habit/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # update habit
        data = {
            "name": "test habit 1",
            "place": "my room3",
            "time": "23:49",
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # validator case 1
        data = {
            "name": "test habit 1",
            "place": "my room3",
            "time": "23:49",
            "is_nice": True,
            "reward": "string",
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # validator case 2
        data = {
            "name": "test habit 1",
            "related": 1,
            "reward": "string",
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # validator case 3
        data = {
            "name": "test habit 13",
            "time_to_complete": 3110,
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # validator case 4
        data = {
            "name": "test habit 13",
            "period": 14,
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # validator case 5
        data = {
            "name": "test habit 13",
            "related": 1,
        }
        response = self.client.put('/habit/update-habit/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # permission safe

        response = self.client.post('/habit/all-habit/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # permission owner
        self.user = User.objects.create(email='user35@example.com', password='test346')
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/habit/get-habit/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
