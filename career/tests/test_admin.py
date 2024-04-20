from unittest.mock import patch

from django.test import TestCase

from ..admin import StudentAdmin
from ..models import Student


class StudentAdminTest(TestCase):
    def setUp(self):
        self.admin = StudentAdmin(Student, None)

    @patch("career.admin.send_mail")
    def test_save_model_creates_student_and_sends_email(self, mock_send_mail):
        # Create a mock request
        request = None  # Set it as needed

        # Create a Student object to save
        obj = Student.objects.create(name="Test Student", email="test@example.com", entry_code="1234567")

        # Call the save_model method
        self.admin.save_model(request, obj, None, False)

        # Assert that the send_mail function was called with the expected arguments
        mock_send_mail.assert_called_once_with(
            "Your Entry Code",
            "Hello Test Student,\n\nYour entry code for www.careercompass.com is: 1234567\n\nPlease keep this code safe and use it for future references.\n\nBest regards,\nYour School Team",
            "admin@careercompass.com",
            ["test@example.com"],
        )

    @patch("career.admin.send_mail")
    def test_save_model_does_not_send_email_on_update(self, mock_send_mail):
        # Create a mock request
        request = None  # Set it as needed

        # Create an existing Student object
        existing_student = Student.objects.create(name="Test Student", email="test@example.com", entry_code="1234567")

        # Call the save_model method with change=True
        self.admin.save_model(request, existing_student, None, True)

        # Assert that send_mail was not called
        mock_send_mail.assert_not_called()
