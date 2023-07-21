from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum, Avg
from itertools import groupby
from django.views.decorators.http import require_POST
from .models import Student, AssessmentScore, Subject
from .forms import AccessForm


def home(request):
    if request.method == "POST":
        form = AccessForm(request.POST)
        if form.is_valid():
            entry_code = form.cleaned_data.get("entry_code")
            request.session["entry_code"] = entry_code
            messages.success(request, "You've been granted access to your Dashboard")
            return redirect("assessment")
        else:
            messages.warning(
                request, "Invalid access code. Please crosscheck and try again"
            )
    else:
        form = AccessForm()

    template = "home.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@require_POST
def end_session(request):
    # Delete the 'code' session variable if it exists
    if "entry_code" in request.session:
        del request.session["entry_code"]

    messages.success(request, "Your session has ended. See you next time.")
    return redirect("home")


def assessment(request):
    entry_code = request.session.get("entry_code")
    try:
        student = Student.objects.get(entry_code=entry_code)
    except Student.DoesNotExist:
        messages.warning(request, "Your entry code session is invalid.")
        del request.session["entry_code"]
        return redirect("home")

    # Calculate the total scores for the student's subjects
    # in each grade level and session term
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
        .order_by("-total_score", "subject__name")
    )

    # Retrieve all assessment scores for the student
    student_assessment_scores = AssessmentScore.objects.filter(student=student)

    # Group the assessment scores by grade level and subject
    assessment_scores_by_grade_subject = {}
    for key, group in groupby(
        student_assessment_scores, key=lambda x: (x.grade_level, x.subject)
    ):
        grade_level, subject = key
        assessment_scores_by_grade_subject.setdefault(grade_level, {}).setdefault(
            subject, []
        ).extend(group)

    # Get the Subject with the highest total score
    highest_subject = assessment_scores_by_grade_subject
    if highest_subject:
        highest_subject = max(
            subject_totals,
            key=lambda subject: subject["total_score"],
        )
        highest_subject["subject_field"] = Subject.objects.get(
            name=highest_subject["subject__name"]
        ).subject_field
    else:
        highest_subject = None

    # Calculate the average total score for each subject across
    # all grade levels and session terms
    subject_average_scores = (
        assessment_scores.values("subject__name")
        .annotate(avg_total_score=Avg("total_score"))
        .order_by("subject__name")
    )

    template = "assessment.html"
    context = {
        "student": student,
        "assessment_scores": assessment_scores,
        "assessment_scores_by_grade_subject": assessment_scores_by_grade_subject,
        "subject_totals": subject_totals,
        "highest_subject": highest_subject,
        "subject_average_scores": subject_average_scores,
    }

    return render(request, template, context)
