from django.test import TestCase
from myapp.models import Status, TicketType
from django.urls import reverse
from myapp.views import CreateStatusPage

class TestStatusModel(TestCase):
    @classmethod
    def create_status_object(self, status_name="Test Status", status_description="This is a test status"):
        status_object =  Status.objects.create(status_name=status_name, status_description=status_description)
        return status_object

    def test_string_creation_for_forms(self):
        status = self.create_status_object()
        status_name = status.__str__()
        self.assertEqual(status_name, "Test Status")

    def test_create_status_form_view(self):
        url = reverse(CreateStatusPage)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

class TestTicketTypeModel(TestCase):
    @classmethod
    def create_ticket_type_object(self, type_name="Test Ticket Type", type_description="This is a test description"):
        return TicketType.objects.create(type_name=type_name, type_description=type_description)

    def test_string_creation(self):
        ticket_type = self.create_ticket_type_object()
        ticket_type_name = ticket_type.__str__()
        self.assertEqual(ticket_type_name, "Test Ticket Type")