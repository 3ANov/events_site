from unittest import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from events.models import Event, Category
from events.views import EventsSet
from users.models import User


class ViewsTestCase(TestCase):
    def setUp(self):

        # Create a test instance
        self.category = Category.objects.create(name="Тестовая категория")
        self.event = Event.objects.create(title="Тестовый заголовок",
                                          description="Тестовое описание",
                                          category=self.category)

        # Create auth user for views using api request factory
        self.username = 'admin@admin.com'
        self.password = 'admin'
        self.user = User.objects.get(email=self.username)

    def tearDown(self):
        pass

    @classmethod
    def setup_class(cls):
        """setup_class() before any methods in this class"""
        pass

    @classmethod
    def teardown_class(cls):
        """teardown_class() after any methods in this class"""
        pass

    def shortDescription(self):
        return None

    def test_view_set1(self):
        """
        No auth example
        """
        api_request = APIRequestFactory().get("events")
        detail_view = EventsSet.as_view(actions={'get': 'retrieve'})
        response = detail_view(api_request, pk=self.event.pk)
        self.assertEqual(response.status_code, 200)

    def test_view_set2(self):
        """
        Auth using force_authenticate
        """
        factory = APIRequestFactory()
        user = User.objects.get(email=self.username)
        detail_view = EventsSet.as_view({'get': 'retrieve'})

        # Make an authenticated request to the view...
        api_request = factory.get('')
        force_authenticate(api_request, user=user)
        response = detail_view(api_request, pk=self.event.pk)
        self.assertEqual(response.status_code, 200)
