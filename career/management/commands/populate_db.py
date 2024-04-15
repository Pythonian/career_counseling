import random

from django.core.management.base import BaseCommand
from faker import Faker

from career.models import (
    AssessmentScore,
    Discipline,
    GradeLevel,
    SessionTerm,
    Student,
    Subject,
    SubjectField,
)

fake = Faker()


def create_grade_levels():
    """
    Create initial GradeLevel objects.
    """
    grade_levels = ["JSS1", "JSS2", "JSS3"]
    for level in grade_levels:
        GradeLevel.objects.get_or_create(name=level)


def create_session_terms():
    """
    Create SessionTerm objects.
    """
    session_terms = ["First Term", "Second Term", "Third Term"]
    for term in session_terms:
        SessionTerm.objects.get_or_create(name=term)


def create_subjects():
    """
    Create subject objects with their disciplines.
    """
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
        # Get or create the SubjectField for the current field_name
        field, _ = SubjectField.objects.get_or_create(name=field_name)

        # Create Subject objects for each subject_name in the subject_list
        for subject_name in subject_list:
            Subject.objects.get_or_create(name=subject_name, subject_field=field)


def create_disciplines():
    disciplines = {
        "General": [
            {
                "name": "Teaching and Education",
                "description": "This discipline focuses on preparing educators and teachers to facilitate learning and development in students of various age groups and educational levels. It covers pedagogy, curriculum design, classroom management, and educational psychology.",
            },
            {
                "name": "Counseling and Psychology",
                "description": "This discipline involves understanding human behavior, emotions, and mental processes to provide support and guidance to individuals facing personal, emotional, or psychological challenges. Counselors and psychologists offer therapeutic interventions and promote mental well-being.",
            },
            {
                "name": "Journalism and Media",
                "description": "This discipline revolves around the production and dissemination of news, information, and content through various media channels such as newspapers, television, radio, and digital platforms. Journalists and media professionals play a vital role in informing and shaping public opinions.",
            },
            {
                "name": "Social Work and Human Services",
                "description": "This discipline aims to improve the well-being of individuals, families, and communities by addressing social issues and providing support services. Social workers and human service professionals assist vulnerable populations, advocate for social justice, and connect people with essential resources.",
            },
            {
                "name": "Religious Studies and Ministry",
                "description": "This discipline involves the academic study of religions, their beliefs, practices, and cultural impact. For those pursuing ministry, it includes training to become religious leaders, clergy, or spiritual guides within their respective faith communities.",
            },
        ],
        "Science": [
            {
                "name": "Research Scientist",
                "description": "Research scientists conduct systematic investigations to expand knowledge and understanding in various scientific fields. They design experiments, collect data, analyze results, and contribute to advancements in their respective domains, ranging from physics and chemistry to biology and beyond.",
            },
            {
                "name": "Medical Doctor or Physician",
                "description": "Medical doctors, also known as physicians, are highly trained healthcare professionals responsible for diagnosing, treating, and preventing illnesses and injuries. They work with patients to provide medical care, prescribe treatments, and promote overall well-being.",
            },
            {
                "name": "Environmental Scientist",
                "description": "Environmental scientists study the natural world and its interactions with human activities. They analyze environmental issues such as pollution, climate change, and conservation efforts. Their research aims to protect the environment and promote sustainable practices.",
            },
            {
                "name": "Data Analyst or Data Scientist",
                "description": "Data analysts and data scientists work with large datasets to extract valuable insights and patterns. They use statistical methods, programming, and machine learning techniques to interpret data and inform decision-making in various industries.",
            },
            {
                "name": "Biotechnologist or Geneticist",
                "description": "Biotechnologists and geneticists explore and manipulate biological systems at the molecular level. They may work on genetic research, develop new therapies, or engineer organisms for various applications, such as pharmaceuticals, agriculture, or biotechnology.",
            },
        ],
        "Technical": [
            {
                "name": "Engineering",
                "description": "Engineers apply scientific principles and mathematics to design, develop, and improve various systems, structures, and technologies. They work in fields such as civil, mechanical, electrical, and computer engineering to create solutions that address societal needs and challenges.",
            },
            {
                "name": "Physical Education and Sports Coaching",
                "description": "This discipline focuses on promoting physical activity and sports engagement for individuals and groups. Physical education instructors teach fitness, sports skills, and health concepts, while sports coaches train athletes to enhance performance and achieve their goals.",
            },
            {
                "name": "Information Technology and Cybersecurity",
                "description": "IT professionals work with computer systems and technology to manage data, develop software, and ensure network security. Cybersecurity specialists protect digital assets from cyber threats, including hackers, viruses, and data breaches.",
            },
            {
                "name": "Home Economics and Nutrition",
                "description": "Home economics encompasses various skills related to managing a household, including cooking, sewing, budgeting, and family resources management. Nutritionists and dieticians specialize in food and dietary choices to promote health and well-being.",
            },
            {
                "name": "Security and Law Enforcement",
                "description": "Professionals in security and law enforcement protect individuals, property, and public safety. They work as police officers, security guards, or investigators, ensuring compliance with laws and responding to emergencies.",
            },
        ],
        "Humanities": [
            {
                "name": "Social Sciences Researcher",
                "description": "Social sciences researchers study human behavior, societies, and cultures. They use scientific methods to investigate social phenomena, conduct surveys, and analyze data to gain insights into social issues and human interactions.",
            },
            {
                "name": "Public Policy and Administration",
                "description": "Professionals in public policy and administration work in government and non-governmental organizations to develop and implement policies, manage public services, and address societal challenges for the welfare of communities and nations.",
            },
            {
                "name": "Archaeologist or Historian",
                "description": "Archaeologists and historians explore the past through artifacts, historical documents, and excavations. They study ancient civilizations, cultures, and events to understand human history and preserve our heritage.",
            },
            {
                "name": "Artist or Fine Arts Professional",
                "description": "Artists and fine arts professionals express creativity through various mediums like painting, sculpture, music, or performance. They contribute to cultural expression, aesthetics, and the enrichment of society through their artistic endeavors.",
            },
            {
                "name": "Cultural Heritage and Museum Curator",
                "description": "Curators in cultural heritage and museums manage and preserve artifacts, artworks, and historical items. They organize exhibitions, conduct research, and contribute to the conservation and presentation of cultural treasures for public enjoyment and education.",
            },
        ],
        "Commercial": [
            {
                "name": "Accounting and Finance",
                "description": "Accounting and finance professionals handle financial records, reporting, and analysis for businesses and organizations. They ensure financial accuracy, manage budgets, and provide financial insights to support decision-making.",
            },
            {
                "name": "Marketing and Advertising",
                "description": "Marketing and advertising experts develop strategies to promote products and services. They conduct market research, create advertising campaigns, and utilize various channels to reach target audiences and increase brand awareness.",
            },
            {
                "name": "Entrepreneurship and Business Management",
                "description": "Entrepreneurs and business managers oversee the operations of their ventures. They take risks, innovate, and make business decisions to achieve growth and success in their enterprises.",
            },
            {
                "name": "Sales and Retail Management",
                "description": "Sales professionals and retail managers handle customer interactions, sales transactions, and manage retail operations. They focus on customer satisfaction, merchandising, and sales growth in retail settings.",
            },
            {
                "name": "Human Resource Management and Recruitment",
                "description": "HR managers and recruiters handle staffing, employee relations, and talent acquisition for organizations. They ensure a skilled and motivated workforce by managing recruitment, training, and employee development.",
            },
        ],
    }

    for field_name, discipline_list in disciplines.items():
        # Get the SubjectField instance for the current field_name
        subject_field = SubjectField.objects.get(name=field_name)

        # Iterate through each discipline_data in the discipline_list
        for discipline_data in discipline_list:
            # Create a Discipline object and the associated SubjectField instance
            Discipline.objects.get_or_create(
                name=discipline_data["name"],
                description=discipline_data["description"],
                subject_field=subject_field,
            )


def create_students(num_students):
    """
    Create dummy Student objects.
    """
    for _ in range(num_students):
        # Create a Student object
        Student.objects.create(
            name=fake.name(),
            entry_code=fake.unique.random_number(digits=7),
            email=fake.email(),
        )


def create_assessment_scores():
    """
    Create dummy AssessmentScore objects.
    """
    # Retrieve all existing GradeLevel, SessionTerm, Subject, and Student objects
    grade_levels = GradeLevel.objects.all()
    session_terms = SessionTerm.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()

    # Iterate through each student
    for student in students:
        # Iterate through each grade level
        for grade_level in grade_levels:
            # Iterate through each session term
            for session_term in session_terms:
                # Iterate through each subject
                for subject in subjects:
                    # Check if an AssessmentScore object with the same combination of fields exists
                    assessment_score, created = AssessmentScore.objects.get_or_create(
                        student=student,
                        grade_level=grade_level,
                        session_term=session_term,
                        subject=subject,
                        defaults={
                            "continuous_assessment": random.randint(0, 40),
                            "exam": random.randint(0, 60),
                        },
                    )

                    # If the object was not created (it already exists), update the scores
                    if not created:
                        assessment_score.continuous_assessment = random.randint(0, 40)
                        assessment_score.exam = random.randint(0, 60)
                        assessment_score.save()


class Command(BaseCommand):
    """
    Custom management command for populating initial data.
    """

    help = "Populate the database with initial data"

    def add_arguments(self, parser):
        parser.add_argument("num_students", type=int, help="Number of students to create")

    def handle(self, *args, **kwargs):
        """
        Main function to create initial data.
        """
        num_students = kwargs["num_students"]

        create_grade_levels()
        create_session_terms()
        create_subjects()
        create_disciplines()
        create_students(num_students)
        create_assessment_scores()
        self.stdout.write(self.style.SUCCESS("Database has been populated successfully!"))
