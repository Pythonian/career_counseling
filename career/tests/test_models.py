from django.db import models
from django.test import TestCase

from ..models import (
    AssessmentScore,
    Discipline,
    GradeLevel,
    SessionTerm,
    Student,
    Subject,
    SubjectField,
)


class GradeLevelTestCase(TestCase):
    def setUp(self):
        GradeLevel.objects.create(name="JSS1")

    def test_grade_level_creation(self):
        """GradeLevel object is created correctly"""
        grade_level = GradeLevel.objects.get(name="JSS1")
        self.assertEqual(grade_level.name, "JSS1")


class SessionTermTestCase(TestCase):
    def setUp(self):
        SessionTerm.objects.create(name="First Term")

    def test_session_term_creation(self):
        """SessionTerm object is created correctly"""
        session_term = SessionTerm.objects.get(name="First Term")
        self.assertEqual(session_term.name, "First Term")


class SubjectFieldTestCase(TestCase):
    def setUp(self):
        SubjectField.objects.create(name="Mathematics")

    def test_subject_field_creation(self):
        """SubjectField object is created correctly"""
        subject_field = SubjectField.objects.get(name="Mathematics")
        self.assertEqual(subject_field.name, "Mathematics")


class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(name="John Doe", email="john@example.com", entry_code="ABC123")

    def test_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_email_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field("email").verbose_name
        self.assertEquals(field_label, "email")

    def test_entry_code_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field("entry_code").verbose_name
        self.assertEquals(field_label, "entry code")

    def test_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_email_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field("email").max_length
        self.assertEquals(max_length, 254)  # EmailField default max_length

    def test_entry_code_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field("entry_code").max_length
        self.assertEquals(max_length, 7)

    def test_unique_entry_code(self):
        student = Student.objects.get(id=1)
        unique = student._meta.get_field("entry_code").unique
        self.assertTrue(unique)

    def test_object_name_is_name(self):
        student = Student.objects.get(id=1)
        expected_object_name = f"{student.name}"
        self.assertEquals(expected_object_name, str(student))


class DisciplineModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        subject_field = SubjectField.objects.create(name="Science")
        Discipline.objects.create(
            name="Physics",
            description="Study of matter and energy",
            subject_field=subject_field,
        )

    def test_name_label(self):
        discipline = Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_description_label(self):
        discipline = Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_subject_field_label(self):
        discipline = Discipline.objects.get(id=1)
        field_label = discipline._meta.get_field("subject_field").verbose_name
        self.assertEquals(field_label, "subject field")

    def test_name_max_length(self):
        discipline = Discipline.objects.get(id=1)
        max_length = discipline._meta.get_field("name").max_length
        self.assertEquals(max_length, 100)

    def test_description_blank(self):
        discipline = Discipline.objects.get(id=1)
        blank = discipline._meta.get_field("description").blank
        # Ensure description field does not allow blank values
        self.assertFalse(blank)

    def test_subject_field_on_delete_protect(self):
        discipline = Discipline.objects.get(id=1)
        on_delete = discipline._meta.get_field("subject_field").remote_field.on_delete
        self.assertEquals(on_delete, models.PROTECT)

    def test_object_name_is_name(self):
        discipline = Discipline.objects.get(id=1)
        expected_object_name = f"{discipline.name}"
        self.assertEquals(expected_object_name, str(discipline))


class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SubjectField.objects.create(name="Science")
        Subject.objects.create(name="Physics", subject_field_id=1)

    def test_name_label(self):
        subject = Subject.objects.get(id=1)
        field_label = subject._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_subject_field_label(self):
        subject = Subject.objects.get(id=1)
        field_label = subject._meta.get_field("subject_field").verbose_name
        self.assertEquals(field_label, "subject field")

    def test_name_max_length(self):
        subject = Subject.objects.get(id=1)
        max_length = subject._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_subject_field_blank(self):
        subject = Subject.objects.get(id=1)
        blank = subject._meta.get_field("subject_field").blank
        self.assertTrue(blank)

    def test_subject_field_null(self):
        subject = Subject.objects.get(id=1)
        null = subject._meta.get_field("subject_field").null
        self.assertTrue(null)

    def test_object_name_is_name(self):
        subject = Subject.objects.get(id=1)
        expected_object_name = f"{subject.name}"
        self.assertEquals(expected_object_name, str(subject))


class SubjectFieldModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SubjectField.objects.create(name="Science")

    def test_name_label(self):
        subject_field = SubjectField.objects.get(id=1)
        field_label = subject_field._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_name_max_length(self):
        subject_field = SubjectField.objects.get(id=1)
        max_length = subject_field._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        subject_field = SubjectField.objects.get(id=1)
        expected_object_name = f"{subject_field.name}"
        self.assertEquals(expected_object_name, str(subject_field))


class SessionTermModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        SessionTerm.objects.create(name="Spring")

    def test_name_label(self):
        session_term = SessionTerm.objects.get(id=1)
        field_label = session_term._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_name_max_length(self):
        session_term = SessionTerm.objects.get(id=1)
        max_length = session_term._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        session_term = SessionTerm.objects.get(id=1)
        expected_object_name = f"{session_term.name}"
        self.assertEquals(expected_object_name, str(session_term))


class GradeLevelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        GradeLevel.objects.create(name="Grade 10")

    def test_name_label(self):
        grade_level = GradeLevel.objects.get(id=1)
        field_label = grade_level._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_name_max_length(self):
        grade_level = GradeLevel.objects.get(id=1)
        max_length = grade_level._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        grade_level = GradeLevel.objects.get(id=1)
        expected_object_name = f"{grade_level.name}"
        self.assertEquals(expected_object_name, str(grade_level))


class AssessmentScoreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        grade_level = GradeLevel.objects.create(name="Grade 10")
        session_term = SessionTerm.objects.create(name="Spring")
        subject = Subject.objects.create(name="Mathematics")
        student = Student.objects.create(name="John Doe", email="john@example.com", entry_code="1234567")
        AssessmentScore.objects.create(
            grade_level=grade_level,
            session_term=session_term,
            subject=subject,
            student=student,
            continuous_assessment=35,
            exam=50,
        )

    def test_grade_level_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("grade_level").verbose_name
        self.assertEquals(field_label, "grade level")

    def test_session_term_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("session_term").verbose_name
        self.assertEquals(field_label, "session term")

    def test_subject_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("subject").verbose_name
        self.assertEquals(field_label, "subject")

    def test_student_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("student").verbose_name
        self.assertEquals(field_label, "student")

    def test_continuous_assessment_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("continuous_assessment").verbose_name
        self.assertEquals(field_label, "continuous assessment")

    def test_exam_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("exam").verbose_name
        self.assertEquals(field_label, "exam")

    def test_total_score_label(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        field_label = assessment_score._meta.get_field("total_score").verbose_name
        self.assertEquals(field_label, "total score")

    def test_grade_level_max_length(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        max_length = assessment_score._meta.get_field("grade_level").max_length
        self.assertEquals(max_length, None)  # ForeignKey fields don't have max_length

    def test_session_term_max_length(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        max_length = assessment_score._meta.get_field("session_term").max_length
        self.assertEquals(max_length, None)  # ForeignKey fields don't have max_length

    def test_subject_max_length(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        max_length = assessment_score._meta.get_field("subject").max_length
        self.assertEquals(max_length, None)  # ForeignKey fields don't have max_length

    def test_continuous_assessment_max_value(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        max_value = assessment_score._meta.get_field("continuous_assessment").validators[1].limit_value
        self.assertEquals(max_value, 40)

    def test_exam_max_value(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        max_value = assessment_score._meta.get_field("exam").validators[1].limit_value
        self.assertEquals(max_value, 60)

    def test_total_score_default(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        default_value = assessment_score._meta.get_field("total_score").default
        self.assertEquals(default_value, 0)

    def test_unique_together(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        unique_together = list(assessment_score._meta.unique_together)
        self.assertEquals(unique_together, [("student", "subject", "session_term", "grade_level")])

    def test_ordering(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        ordering = assessment_score._meta.ordering
        self.assertEquals(ordering, ["grade_level", "session_term"])

    def test_calculate_total_score(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        total_score = assessment_score.calculate_total_score()
        self.assertEquals(total_score, 85)

    def test_str_method(self):
        assessment_score = AssessmentScore.objects.get(id=1)
        expected_str = f"{assessment_score.subject} - {assessment_score.session_term} - {assessment_score.grade_level} - {assessment_score.continuous_assessment}/{assessment_score.exam}/{assessment_score.calculate_total_score()}"
        self.assertEquals(expected_str, str(assessment_score))
