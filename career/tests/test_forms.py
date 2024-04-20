from django.test import TestCase

from ..forms import AccessForm
from ..models import Student


class AccessFormTestCase(TestCase):
    def test_valid_entry_code(self):
        """Test valid entry code"""
        # Create a student with a valid entry code
        valid_entry_code = "ABCD123"
        Student.objects.create(name="Test Student", email="test@example.com", entry_code=valid_entry_code)

        # Create a form with the valid entry code
        form_data = {"entry_code": valid_entry_code}
        form = AccessForm(data=form_data)

        # Check that the form is valid
        self.assertTrue(form.is_valid())

    def test_invalid_entry_code(self):
        """Test invalid entry code"""
        # Create a form with an invalid entry code
        invalid_entry_code = "INVALID"
        form_data = {"entry_code": invalid_entry_code}
        form = AccessForm(data=form_data)

        # Check that the form is invalid
        self.assertFalse(form.is_valid())
        # Check that the form error message matches the expected message
        self.assertEqual(form.errors["entry_code"], ["Invalid access code. Please crosscheck and try again."])

    def test_missing_entry_code(self):
        """Test missing entry code"""
        # Create a form with a missing entry code
        form_data = {}  # No entry code provided
        form = AccessForm(data=form_data)

        # Check that the form is invalid
        self.assertFalse(form.is_valid())
        # Check that the form error message matches the expected message
        self.assertEqual(form.errors["entry_code"], ["This field is required."])
