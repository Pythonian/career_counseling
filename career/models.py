from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    """A model with timestamp fields for creation and last update."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GradeLevel(TimestampedModel):
    """
    Model representing a grade level instance.
    """

    name = models.CharField(
        _("name"),
        max_length=50,
        unique=True,
        help_text=_("Enter the name of the grade level."),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Grade Level")
        verbose_name_plural = _("Grade Levels")

    def __str__(self):
        """
        Return a string representation of the grade level.
        """
        return self.name


class SessionTerm(TimestampedModel):
    """
    Model representing a session term instance.
    """

    name = models.CharField(
        _("name"),
        max_length=50,
        unique=True,
        help_text=_("Enter the name of the session term."),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Session Term")
        verbose_name_plural = _("Session Terms")

    def __str__(self):
        """
        Return a string representation of the session term.
        """
        return self.name


class SubjectField(TimestampedModel):
    """
    Model representing a subject field instance.
    """

    name = models.CharField(
        _("name"),
        max_length=50,
        unique=True,
        help_text=_("Enter the name of the subject field."),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Subject Field")
        verbose_name_plural = _("Subject Fields")

    def __str__(self):
        """
        Return a string representation of the subject field.
        """
        return self.name


class Subject(TimestampedModel):
    """
    Model representing a subject instance.
    """

    name = models.CharField(
        _("name"),
        max_length=50,
        unique=True,
        help_text=_("Enter the name of the subject."),
    )

    subject_field = models.ForeignKey(
        SubjectField,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=_("subject field"),
        help_text=_("Select the subject field associated with this subject."),
    )

    class Meta:
        ordering = ["subject_field"]
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        """
        Return a string representation of the subject.
        """
        return self.name


class Discipline(TimestampedModel):
    """
    Model representing a discipline instance.
    """

    name = models.CharField(
        _("name"),
        max_length=100,
        help_text=_("Enter the name of the discipline."),
    )

    description = models.TextField(
        _("description"),
        help_text=_("Enter a description for the discipline."),
    )

    subject_field = models.ForeignKey(
        SubjectField,
        on_delete=models.PROTECT,
        verbose_name=_("subject field"),
        help_text=_("Select the subject field associated with this discipline."),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")

    def __str__(self):
        """
        Return a string representation of the discipline.
        """
        return self.name


class Student(TimestampedModel):
    """
    Model representing a student instance.
    """

    name = models.CharField(
        _("name"),
        max_length=50,
        help_text=_("Enter the name of the student."),
    )

    email = models.EmailField(
        _("email"),
        help_text=_("Enter the email address of the student."),
    )

    entry_code = models.CharField(
        _("entry code"),
        max_length=7,
        unique=True,
        help_text=_("Enter the unique entry code for the student."),
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        """
        Return a string representation of the student.
        """
        return self.name


class AssessmentScore(TimestampedModel):
    """
    Model representing assessment scores for students.
    """

    grade_level = models.ForeignKey(
        GradeLevel,
        on_delete=models.CASCADE,
        verbose_name=_("grade level"),
        help_text=_("Select the grade level for the assessment score."),
    )

    session_term = models.ForeignKey(
        SessionTerm,
        on_delete=models.CASCADE,
        verbose_name=_("session term"),
        help_text=_("Select the session term for the assessment score."),
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name=_("subject"),
        help_text=_("Select the subject for the assessment score."),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("student"),
        help_text=_("Select the student associated with the assessment score."),
    )

    continuous_assessment = models.PositiveIntegerField(
        _("continuous assessment"),
        validators=[MinValueValidator(0), MaxValueValidator(40)],
        help_text=_("Enter the continuous assessment score (0-40)."),
    )

    exam = models.PositiveIntegerField(
        _("exam"),
        validators=[MinValueValidator(0), MaxValueValidator(60)],
        help_text=_("Enter the exam score (0-60)."),
    )

    total_score = models.PositiveIntegerField(
        _("total score"),
        default=0,
        help_text=_("Total score calculated as sum of continuous assessment and exam scores."),
    )

    class Meta:
        unique_together = ["student", "subject", "session_term", "grade_level"]
        ordering = ["grade_level", "session_term"]
        verbose_name = _("Assessment Score")
        verbose_name_plural = _("Assessment Scores")

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
