from django.contrib.auth.models import User
from django.test import TestCase

from career.templatetags.template_tags import sum_total_scores

from ..models import AssessmentScore, GradeLevel, SessionTerm, Student, Subject


class TemplateTagTest(TestCase):
    def setUp(self):
        self.grade_level = GradeLevel.objects.create(name="JSS1")
        self.session_term1 = SessionTerm.objects.create(name="First Term")
        self.session_term2 = SessionTerm.objects.create(name="Second Term")
        self.subject = Subject.objects.create(name="Mathematics")
        self.student = Student.objects.create(name="John Doe", email="john@example.com", entry_code="1234567")
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Create AssessmentScore objects with unique combinations of student, subject, session_term, and grade_level
        self.score1 = AssessmentScore.objects.create(
            grade_level=self.grade_level,
            session_term=self.session_term1,
            subject=self.subject,
            student=self.student,
            continuous_assessment=30,
            exam=70,
        )
        self.score2 = AssessmentScore.objects.create(
            grade_level=self.grade_level,
            session_term=self.session_term2,
            subject=self.subject,
            student=self.student,
            continuous_assessment=40,
            exam=60,
        )

    def test_sum_total_scores(self):
        # Call the template filter with the AssessmentScore objects
        total_score = sum_total_scores([self.score1, self.score2])

        # Calculate the expected total score manually
        expected_total_score = self.score1.total_score + self.score2.total_score

        # Assert that the total score returned by the template filter matches the expected total score
        self.assertEqual(total_score, expected_total_score)
