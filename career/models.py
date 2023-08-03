from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class GradeLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SessionTerm(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubjectField(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subject_field = models.ForeignKey(
        SubjectField, on_delete=models.PROTECT, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject_field = models.ForeignKey(SubjectField, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    entry_code = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.name


class AssessmentScore(models.Model):
    grade_level = models.ForeignKey(GradeLevel, on_delete=models.CASCADE)
    session_term = models.ForeignKey(SessionTerm, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    continuous_assessment = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(40)]
    )
    exam = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(60)]
    )
    total_score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["student", "subject", "session_term", "grade_level"]
        ordering = ["grade_level", "session_term"]

    def calculate_total_score(self):
        return self.continuous_assessment + self.exam

    def save(self, *args, **kwargs):
        self.total_score = self.calculate_total_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject} - {self.session_term} - {self.grade_level} - {self.continuous_assessment}/{self.exam}/{self.calculate_total_score()}"
