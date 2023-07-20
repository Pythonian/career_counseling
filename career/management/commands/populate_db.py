# from django.core.management.base import BaseCommand
# from career.models import (
#     GradeLevel,
#     SessionTerm,
#     SubjectField,
#     Subject,
#     Student,
#     AssessmentScore,
# )
# from django.contrib.auth.models import User
# from faker import Faker
# from random import randint


# class Command(BaseCommand):
#     help = "Populate the database with initial data"

#     def handle(self, *args, **kwargs):
#         self.create_grade_levels()
#         self.create_session_terms()
#         self.create_subject_fields()
#         self.create_subjects()
#         self.create_students_and_scores()

#     def create_grade_levels(self):
#         grade_levels = ["JS1", "JS2", "JS3"]
#         for name in grade_levels:
#             GradeLevel.objects.get_or_create(name=name)
#         self.stdout.write(self.style.SUCCESS("Successfully created Grade Levels"))

#     def create_session_terms(self):
#         session_terms = ["First Term", "Second Term", "Third Term"]
#         for name in session_terms:
#             SessionTerm.objects.get_or_create(name=name)
#         self.stdout.write(self.style.SUCCESS("Successfully created Session Terms"))

#     def create_subject_fields(self):
#         subject_fields = ["Science", "Technical", "Humanities", "Commercial"]
#         for name in subject_fields:
#             SubjectField.objects.get_or_create(name=name)
#         self.stdout.write(self.style.SUCCESS("Successfully created Subject Fields"))

#     def create_subjects(self):
#         subjects_data = {
#             "Science": [
#                 "Mathematics",
#                 "Basic Science",
#                 "Information and Communications Technology",
#                 "Agricultural Science",
#             ],
#             "Technical": [
#                 "Basic Technology",
#                 "Physical and Health Education",
#                 "Security Education",
#                 "Home Economics",
#             ],
#             "Humanities": [
#                 "English",
#                 "Social Studies",
#                 "Civic Education",
#                 "Igbo",
#                 "History",
#                 "Creative and Cultural Arts",
#                 "Christian Religious Studies",
#             ],
#             "Commercial": ["Business Studies"],
#         }

#         for field_name, subjects in subjects_data.items():
#             field = SubjectField.objects.get(name=field_name)
#             for name in subjects:
#                 Subject.objects.get_or_create(name=name, subject_field=field)
#             self.stdout.write(
#                 self.style.SUCCESS(f"Successfully created subjects for {field_name}")
#             )

#         self.stdout.write(self.style.SUCCESS("Successfully created Subjects"))

#     # def create_students_and_scores(self):
#     #     fake = Faker()

#     #     grade_levels = GradeLevel.objects.all()
#     #     session_terms = SessionTerm.objects.all()
#     #     subjects = Subject.objects.all()

#     #     for grade_level in grade_levels:
#     #         for session_term in session_terms:
#     #             for subject in subjects:
#     #                 num_students = randint(
#     #                     5, 10
#     #                 )  # Random number of students per subject
#     #                 for _ in range(num_students):
#     #                     # Create a fake student
#     #                     student_name = fake.name()
#     #                     entry_code = fake.unique.random_number(digits=7)
#     #                     student, _ = Student.objects.get_or_create(
#     #                         name=student_name, entry_code=entry_code
#     #                     )

#     #                     # Generate random continuous assessment and exam scores
#     #                     continuous_assessment = randint(0, 40)
#     #                     exam = randint(0, 60)

#     #                     # Create AssessmentScore for the student
#     #                     AssessmentScore.objects.create(
#     #                         grade_level=grade_level,
#     #                         session_term=session_term,
#     #                         subject=subject,
#     #                         student=student,
#     #                         continuous_assessment=continuous_assessment,
#     #                         exam=exam,
#     #                     )

#     #     self.stdout.write(
#     #         self.style.SUCCESS(
#     #             "Successfully created fake students and assessment scores"
#     #         )
#     #     )

#     def create_students_and_scores(self):
#         fake = Faker()

#         grade_levels = GradeLevel.objects.all()
#         session_terms = SessionTerm.objects.all()
#         subjects = Subject.objects.all()

#         for grade_level in grade_levels:
#             for session_term in session_terms:
#                 for subject in subjects:
#                     # Create a fake student
#                     student_name = fake.name()
#                     entry_code = fake.unique.random_number(digits=7)
#                     student, _ = Student.objects.get_or_create(
#                         name=student_name, entry_code=entry_code
#                     )

#                     # Generate random continuous assessment and exam scores
#                     continuous_assessment = randint(0, 40)
#                     exam = randint(0, 60)

#                     # Create AssessmentScore for the student
#                     AssessmentScore.objects.create(
#                         grade_level=grade_level,
#                         session_term=session_term,
#                         subject=subject,
#                         student=student,
#                         continuous_assessment=continuous_assessment,
#                         exam=exam,
#                     )

#         self.stdout.write(
#             self.style.SUCCESS(
#                 "Successfully created fake students and assessment scores"
#             )
#         )

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
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
    grade_levels = ["JS1", "JS2", "JS3"]
    for level in grade_levels:
        GradeLevel.objects.create(name=level)


def create_session_terms():
    session_terms = ["First Term", "Second Term", "Third Term"]
    for term in session_terms:
        SessionTerm.objects.create(name=term)


def create_subjects():
    subjects = {
        "Science": [
            "Mathematics",
            "Basic Science",
            "Information and Communications Technology",
            "Agricultural Science",
        ],
        "Technical": [
            "Basic Technology",
            "Physical and Health Education",
            "Security Education",
            "Home Economics",
        ],
        "Humanities": [
            "English",
            "Social Studies",
            "Civic Education",
            "Igbo",
            "History",
            "Creative and Cultural Arts",
            "Christian Religious Studies",
            "Islamic Religious Studies",
        ],
        "Commercial": ["Business Studies"],
    }

    for field_name, subject_list in subjects.items():
        field, _ = SubjectField.objects.get_or_create(name=field_name)
        for subject_name in subject_list:
            Subject.objects.create(name=subject_name, subject_field=field)


def create_students():
    for _ in range(2):
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
