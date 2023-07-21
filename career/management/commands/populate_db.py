import random
from django.core.management.base import BaseCommand
from faker import Faker
from career.models import (
    GradeLevel,
    SessionTerm,
    Subject,
    SubjectField,
    Student,
    AssessmentScore,
)

fake = Faker()


def create_grade_levels():
    grade_levels = ["JSS1", "JSS2", "JSS3"]
    for level in grade_levels:
        GradeLevel.objects.create(name=level)


def create_session_terms():
    session_terms = ["First Term", "Second Term", "Third Term"]
    for term in session_terms:
        SessionTerm.objects.create(name=term)


def create_subjects():
    subjects = {
        "General": [
            "Mathematics",
            "English",
            "Igbo",
            "Christian Religious Studies",
        ],
        "Science": [
            "Basic Science",
            "Information Technology",
            "Agricultural Science",
        ],
        "Technical": [
            "Basic Technology",
            "Physical and Health Education",
            "Security Education",
            "Home Economics",
        ],
        "Humanities": [
            "Social Studies",
            "Civic Education",
            "History",
            "Creative and Cultural Arts",
        ],
        "Commercial": ["Business Studies"],
    }

    for field_name, subject_list in subjects.items():
        field, _ = SubjectField.objects.get_or_create(name=field_name)
        for subject_name in subject_list:
            Subject.objects.create(name=subject_name, subject_field=field)


def create_students():
    for _ in range(3):
        Student.objects.create(
            name=fake.name(), entry_code=fake.unique.random_number(digits=7)
        )


def create_assessment_scores():
    grade_levels = GradeLevel.objects.all()
    session_terms = SessionTerm.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()

    for student in students:
        for grade_level in grade_levels:
            for session_term in session_terms:
                for subject in subjects:
                    continuous_assessment = random.randint(0, 40)
                    exam = random.randint(0, 60)
                    total_score = continuous_assessment + exam

                    AssessmentScore.objects.create(
                        student=student,
                        grade_level=grade_level,
                        session_term=session_term,
                        subject=subject,
                        continuous_assessment=continuous_assessment,
                        exam=exam,
                        total_score=total_score,
                    )


class Command(BaseCommand):
    help = "Populate the database with initial data"

    def handle(self, *args, **kwargs):
        create_grade_levels()
        create_session_terms()
        create_subjects()
        create_students()
        create_assessment_scores()
        self.stdout.write(
            self.style.SUCCESS("Database has been populated successfully!")
        )
