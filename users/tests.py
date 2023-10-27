from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserAPITest(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_user_create(self):
        data = {'email': 'user@example.com', 'password': 'Qf1fgj_45ty14$'}
        response = self.client.post('/user/create-user/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
