from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from events.models import Event


class EventTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new event object.
        """

        data = {
            "title": "Новый ивент 22",
            "description": "Новое описание ивента",
            "event_instances": [
                {
                    "place": {
                        "geom": {
                            "latitude": 50.736455,
                            "longitude": 66.09375
                        },
                        "name": "Новый",
                        "city": "Урюпинск"
                    },
                    "time_start": "2020-10-19T16:16:03Z",
                    "time_end": "2020-10-19T16:16:04Z"
                }
            ],
            "category": 1
        }

        client = APIClient()
        client.login(username='admin@admin.com', password='admin')
        response = client.post('http://127.0.0.1/api/events/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Event.objects.get().title, 'Новый ивент 22')