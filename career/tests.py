from django.test import TestCase

from .models import GradeLevel, SessionTerm, SubjectField


class GradeLevelTestCase(TestCase):
    def setUp(self):
        GradeLevel.objects.create(name="Grade 1")

    def test_grade_level_creation(self):
        """GradeLevel object is created correctly"""
        grade_level = GradeLevel.objects.get(name="Grade 1")
        self.assertEqual(grade_level.name, "Grade 1")


class SessionTermTestCase(TestCase):
    def setUp(self):
        SessionTerm.objects.create(name="Term 1")

    def test_session_term_creation(self):
        """SessionTerm object is created correctly"""
        session_term = SessionTerm.objects.get(name="Term 1")
        self.assertEqual(session_term.name, "Term 1")


class SubjectFieldTestCase(TestCase):
    def setUp(self):
        SubjectField.objects.create(name="Mathematics")

    def test_subject_field_creation(self):
        """SubjectField object is created correctly"""
        subject_field = SubjectField.objects.get(name="Mathematics")
        self.assertEqual(subject_field.name, "Mathematics")
