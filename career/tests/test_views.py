from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from ..forms import AccessForm
from ..models import Student
from ..views import end_session


class HomeViewTest(TestCase):
    def setUp(self):
        # Create a sample student for testing
        self.student = Student.objects.create(name="John Doe", email="john@example.com", entry_code="1234567")

        # Create a test user for session
        self.user = User.objects.create(username="testuser", password="12345")

        # Create a request factory
        self.factory = RequestFactory()

    def test_home_view_get(self):
        # Test GET request to the home view
        url = reverse("home")
        response = self.client.get(url)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, "home.html")

        # Check if the form is present in the context
        self.assertIsInstance(response.context["form"], AccessForm)

    def test_home_view_post_valid(self):
        # Test POST request with valid data
        url = reverse("home")
        data = {"entry_code": self.student.entry_code}
        response = self.client.post(url, data)

        # Check if the user is redirected to the assessment page
        self.assertRedirects(response, reverse("assessment"))

        # Check if success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You've been granted access to your Dashboard")

        # Check if entry code is stored in the session
        self.assertEqual(response.wsgi_request.session["entry_code"], self.student.entry_code)

    def test_home_view_post_invalid(self):
        # Test POST request with invalid data
        url = reverse("home")
        data = {"entry_code": "invalid_code"}
        response = self.client.post(url, data)

        # Check if the user stays on the same page
        self.assertEqual(response.status_code, 200)

        # Check if warning message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Invalid access code. Please crosscheck and try again")

    def test_home_view_form_submission(self):
        # Create a test client
        client = Client()

        # Test form submission
        response = client.post(reverse("home"), {"entry_code": self.student.entry_code})

        # Check if the user is redirected to the assessment page
        self.assertRedirects(response, reverse("assessment"))

        # Check if success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You've been granted access to your Dashboard")

        # Check if entry code is stored in the session
        self.assertEqual(response.client.session["entry_code"], self.student.entry_code)


class EndSessionViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_end_session_success(self):
        # Create a session with 'entry_code' variable
        request = self.factory.post(reverse("end_session"))
        setattr(request, "session", {"entry_code": "some_entry_code"})
        setattr(request, "_messages", FallbackStorage(request))

        # Call the end_session view function
        response = end_session(request)

        # Check if the 'entry_code' session variable is deleted
        self.assertNotIn("entry_code", request.session)

        # Check if the view redirects to the home page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))

        # Check if success message is displayed
        storage = messages.get_messages(request)
        storage.used = True
        self.assertTrue(storage)
        self.assertEqual(str(list(storage)[0]), "Your session has ended. See you next time.")
