from django import forms
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from itertools import groupby
from .models import Student, AssessmentScore


class AccessForm(forms.Form):
    entry_code = forms.CharField(max_length=10)

    def clean_entry_code(self):
        entry_code = self.cleaned_data.get("entry_code")
        try:
            Student.objects.get(entry_code=entry_code)
        except Student.DoesNotExist:
            raise forms.ValidationError("Invalid code")
        return entry_code


def home(request):
    if request.method == "POST":
        form = AccessForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get("entry_code")
            request.session["code"] = code
            return redirect("assessment")
        else:
            messages.warning(request, "Invalid access code.")
    else:
        form = AccessForm()

    template = "home.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def assessment(request):
    code = request.session.get("code")
    try:
        student = Student.objects.get(entry_code=code)
    except Student.DoesNotExist:
        return redirect("home")

    # Calculate the total scores for the student's subjects in each grade level and session term
    assessment_scores = (
        AssessmentScore.objects.filter(student=student)
        .values("grade_level__name", "session_term__name", "subject__name")
        .annotate(
            continuous_assessment_total=Sum("continuous_assessment"),
            exam_total=Sum("exam"),
        )
    )

    # Calculate the total score for each entry in assessment_scores
    for entry in assessment_scores:
        entry["total_score"] = (
            entry["continuous_assessment_total"] + entry["exam_total"]
        )

    # Calculate the subject totals for the student
    subject_totals = (
        assessment_scores.values("subject__name")
        .annotate(total_score=Sum("total_score"))
        .order_by("subject__name")
    )

    # Retrieve all assessment scores for the student
    assessment_scores2 = AssessmentScore.objects.filter(student=student)

    # Group the assessment scores by grade level and subject
    assessment_scores_by_grade_subject = {}
    for key, group in groupby(
        assessment_scores2, key=lambda x: (x.grade_level, x.subject)
    ):
        grade_level, subject = key
        assessment_scores_by_grade_subject.setdefault(grade_level, {}).setdefault(
            subject, []
        ).extend(group)

    template = "assessment.html"
    context = {
        "student": student,
        "assessment_scores": assessment_scores,
        "assessment_scores2": assessment_scores2,
        "assessment_scores_by_grade_subject": assessment_scores_by_grade_subject,
        "subject_totals": subject_totals,
    }

    return render(request, template, context)
