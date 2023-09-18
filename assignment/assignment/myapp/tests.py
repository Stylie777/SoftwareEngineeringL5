from django.test import TestCase
from myapp.models import Status, TicketType
from django.urls import reverse
from myapp.views import (
    CreateStatusPage,
    ViewStatuses,
    ViewStatus,
    UpdateStatus,
    DeleteStatus,
    CreateTicketTypePage,
    ViewTypes,
    ViewType,
    UpdateTicketType,
    DeleteTicketType,
    CreateTicketPage,
    ViewTickets,
    ViewTicket,
    UpdateTicket,
    DeleteTicket,
)
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from myapp.forms import AddStatus, AddTicketType, Ticket, AddTicket
import datetime


class TestStatusModel(TestCase):
    def create_status_object(
        self, status_name="Test Status", status_description="This is a test status"
    ):
        status_object = Status.objects.create(
            status_name=status_name, status_description=status_description
        )
        return status_object

    def test_string_creation_for_forms(self):
        status = self.create_status_object()
        status_name = status.__str__()
        self.assertEqual(status_name, "Test Status")

    def create_user(self):
        self.user = User.objects.create_user(
            username="Test Account", email="test@test.com", password="TestPassword"
        )

    def get_response_code(self, url) -> int:
        return self.client.get(url).status_code

    def test_create_status_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(CreateStatusPage)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_statuses_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(ViewStatuses)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_status_view_response_code(self):
        self.create_status_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(ViewStatus, args=["Test Status"])
        self.assertEqual(self.get_response_code(url), 200)

    def test_update_status_view_response_code(self):
        self.create_status_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(UpdateStatus, args=["Test Status"])
        self.assertEqual(self.get_response_code(url), 200)

    def create_super_user(self):
        self.user = User.objects.create_superuser(
            username="Test Account Admin",
            email="testadmin@test.com",
            password="TestPassword",
        )

    def test_delete_status_view_response_code(self):
        self.create_status_object()
        self.create_super_user()
        self.client.login(username="Test Account Admin", password="TestPassword")
        url = reverse(DeleteStatus, args=["Test Status"])
        self.assertEqual(self.get_response_code(url), 200)

    def create_status_form(
        self, status_name: str, status_description: str
    ) -> AddStatus:
        data = {"status_name": status_name, "status_description": status_description}
        return AddStatus(data=data)

    def test_add_status_form_when_name_does_not_have_capital_letter_at_start_of_type_name(
        self,
    ):
        form = self.create_status_form("test Status", "This is a test")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_does_not_exist(self):
        form = self.create_status_form("", "This is a test")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_has_capital_letter_at_start_of_type_name(self):
        form = self.create_status_form("Test Status", "This is a test")
        result = form.is_valid()
        self.assertTrue(result)


class TestTicketTypeModel(TestCase):
    def create_ticket_type_object(
        self,
        type_name="Test Ticket Type",
        type_description="This is a test description",
    ):
        return TicketType.objects.create(
            type_name=type_name, type_description=type_description
        )

    def test_string_creation(self):
        ticket_type = self.create_ticket_type_object()
        ticket_type_name = ticket_type.__str__()
        self.assertEqual(ticket_type_name, "Test Ticket Type")

    def create_user(self):
        self.user = User.objects.create_user(
            username="Test Account", email="test@test.com", password="TestPassword"
        )

    def get_response_code(self, url: str) -> int:
        return self.client.get(url).status_code

    def test_create_ticket_type_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(CreateTicketTypePage)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_statuses_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(ViewTypes)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_status_view_response_code(self):
        self.create_ticket_type_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(ViewType, args=["Test Ticket Type"])
        self.assertEqual(self.get_response_code(url), 200)

    def test_update_status_view_response_code(self):
        self.create_ticket_type_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(UpdateTicketType, args=["Test Ticket Type"])
        self.assertEqual(self.get_response_code(url), 200)

    def create_super_user(self):
        self.user = User.objects.create_superuser(
            username="Test Account Admin",
            email="testadmin@test.com",
            password="TestPassword",
        )

    def test_delete_status_view_response_code(self):
        self.create_ticket_type_object()
        self.create_super_user()
        self.client.login(username="Test Account Admin", password="TestPassword")
        url = reverse(DeleteTicketType, args=["Test Ticket Type"])
        self.assertEqual(self.get_response_code(url), 200)

    def create_ticket_type_form(
        self, type_name: str, type_description: str
    ) -> AddTicketType:
        data = {"type_name": type_name, "type_description": type_description}
        return AddTicketType(data=data)

    def test_add_ticket_type_form_when_name_does_not_have_capital_letter_at_start_of_string(
        self,
    ):
        form = self.create_ticket_type_form("test Type", "This is a test")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_does_not_exist(self):
        form = self.create_ticket_type_form("", "This is a test")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_has_capital_letter_at_start(self):
        form = self.create_ticket_type_form("Test Type", "This is a test")
        result = form.is_valid()
        self.assertTrue(result)


class TestTicketModel(TestCase):
    status_model = TestStatusModel()
    type_model = TestTicketTypeModel()

    def create_ticket_object(self, ticket_title="Test Ticket Title"):
        status_object = self.status_model.create_status_object()
        type_object = self.type_model.create_ticket_type_object()
        return Ticket.objects.create(
            ticket_title=ticket_title,
            date_reported=datetime.date.today(),
            status_id=status_object,
            type_id=type_object,
        )

    def create_user(self):
        self.user = User.objects.create_user(
            username="Test Account", email="test@test.com", password="TestPassword"
        )

    def get_response_code(self, url: str) -> int:
        return self.client.get(url).status_code

    def test_create_ticket_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(CreateTicketPage)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_tickets_view_response_code(self):
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        url = reverse(ViewTickets)
        self.assertEqual(self.get_response_code(url), 200)

    def test_view_ticket_view_response_code(self):
        self.create_ticket_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        ticket = Ticket.objects.get(ticket_title="Test Ticket Title")
        url = reverse(ViewTicket, args=[ticket.ticket_id])
        self.assertEqual(self.get_response_code(url), 200)

    def test_update_ticket_view_response_code(self):
        self.create_ticket_object()
        self.create_user()
        self.client.login(username="Test Account", password="TestPassword")
        ticket = Ticket.objects.get(ticket_title="Test Ticket Title")
        url = reverse(UpdateTicket, args=[ticket.ticket_id])
        self.assertEqual(self.get_response_code(url), 200)

    def create_super_user(self):
        self.user = User.objects.create_superuser(
            username="Test Account Admin",
            email="testadmin@test.com",
            password="TestPassword",
        )

    def test_delete_ticket_view_response_code(self):
        self.create_ticket_object()
        self.create_super_user()
        self.client.login(username="Test Account Admin", password="TestPassword")
        ticket = Ticket.objects.get(ticket_title="Test Ticket Title")
        url = reverse(DeleteTicket, args=[ticket.ticket_id])
        self.assertEqual(self.get_response_code(url), 200)

    def create_ticket_form(self, ticket_title: str) -> AddTicketType:
        data = {
            "ticket_title": ticket_title,
            "status": self.status_model.create_status_object(),
            "type": self.type_model.create_ticket_type_object(),
        }
        return AddTicket(data=data)

    def test_add_ticket_form_when_name_does_not_have_capital_letter_at_start_of_string(
        self,
    ):
        form = self.create_ticket_form("test Ticket")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_does_not_exist(self):
        form = self.create_ticket_form("")
        self.assertFalse(form.is_valid())

    def test_add_status_form_when_name_has_capital_letter_at_start(self):
        form = self.create_ticket_form("Test Ticket")
        result = form.is_valid()
        self.assertTrue(result)
