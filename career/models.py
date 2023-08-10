from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GradeLevel(models.Model):
    """
    Model representing the grade levels.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the grade level.",
    )

    def __str__(self):
        """
        Return a string representation of the grade level.
        """
        return self.name


class SessionTerm(models.Model):
    """
    Model representing the session terms.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the session term.",
    )

    def __str__(self):
        """
        Return a string representation of the session term.
        """
        return self.name


class SubjectField(models.Model):
    """
    Model representing subject fields.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the subject field.",
    )

    def __str__(self):
        """
        Return a string representation of the subject field.
        """
        return self.name


class Subject(models.Model):
    """
    Model representing subjects.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the name of the subject.",
    )

    subject_field = models.ForeignKey(
        SubjectField,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="Select the subject field associated with this subject.",
    )

    def __str__(self):
        """
        Return a string representation of the subject.
        """
        return self.name


class Discipline(models.Model):
    """
    Model representing disciplines.
    """

    name = models.CharField(
        max_length=100,
        help_text="Enter the name of the discipline.",
    )

    description = models.TextField(
        help_text="Enter a description for the discipline.",
    )

    subject_field = models.ForeignKey(
        SubjectField,
        on_delete=models.PROTECT,
        help_text="Select the subject field associated with this discipline.",
    )

    def __str__(self):
        """
        Return a string representation of the discipline.
        """
        return self.name


class Student(models.Model):
    """
    Model representing students.
    """

    name = models.CharField(
        max_length=50,
        help_text="Enter the name of the student.",
    )

    email = models.EmailField(
        help_text="Enter the email address of the student.",
    )

    entry_code = models.CharField(
        max_length=7,
        unique=True,
        help_text="Enter the unique entry code for the student.",
    )

    def __str__(self):
        """
        Return a string representation of the student.
        """
        return self.name


class AssessmentScore(models.Model):
    """
    Model representing assessment scores for students.
    """

    grade_level = models.ForeignKey(
        GradeLevel,
        on_delete=models.CASCADE,
        help_text="Select the grade level for the assessment score.",
    )

    session_term = models.ForeignKey(
        SessionTerm,
        on_delete=models.CASCADE,
        help_text="Select the session term for the assessment score.",
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        help_text="Select the subject for the assessment score.",
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        help_text="Select the student associated with the assessment score.",
    )

    continuous_assessment = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(40)],
        help_text="Enter the continuous assessment score (0-40).",
    )

    exam = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(60)],
        help_text="Enter the exam score (0-60).",
    )

    total_score = models.PositiveIntegerField(
        default=0,
        help_text="Total score calculated as sum of continuous assessment and exam scores.",
    )

    class Meta:
        unique_together = ["student", "subject", "session_term", "grade_level"]
        ordering = ["grade_level", "session_term"]

    def calculate_total_score(self):
        """
        Calculate the total score by summing continuous assessment and exam scores.
        """
        return self.continuous_assessment + self.exam

    def save(self, *args, **kwargs):
        """
        Override the save method to calculate and update the total score.
        """
        self.total_score = self.calculate_total_score()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a string representation of the assessment score.
        """
        return f"{self.subject} - {self.session_term} - {self.grade_level} - {self.continuous_assessment}/{self.exam}/{self.calculate_total_score()}"
