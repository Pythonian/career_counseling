from itertools import groupby

from django.contrib import messages
from django.db.models import Avg, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import AccessForm
from .models import AssessmentScore, Discipline, Student, Subject


def home(request):
    """
    View function for the home page.

    Handles access form submission, validation, and redirection.
    """
    # If the HTTP request method is a Post request
    if request.method == "POST":
        # Pass in the Post data into the AccessForm
        form = AccessForm(request.POST)
        # If the form has been certified to be valid, no errors
        if form.is_valid():
            # Get the entered entry code from the form
            entry_code = form.cleaned_data.get("entry_code")

            # Store the entry code in the session
            request.session["entry_code"] = entry_code

            # Display a success message and redirect to the assessment page
            messages.success(request, "You've been granted access to your Dashboard")
            return redirect("assessment")
        else:
            # Display a warning message for invalid access code
            messages.warning(request, "Invalid access code. Please crosscheck and try again")
    else:
        # Create a new AccessForm instance for GET requests
        form = AccessForm()

    template = "home.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@require_POST
def end_session(request):
    """
    View function for ending a user's session.

    Deletes the 'entry_code' session variable if it exists
    and displays a success message.
    """
    if "entry_code" in request.session:
        # Delete the 'entry_code' session variable
        del request.session["entry_code"]

    # Display a success message and redirect to the home page
    messages.success(request, "Your session has ended. See you next time.")
    return redirect("home")


def assessment(request):
    """
    View function for the assessment page.

    Retrieves assessment scores and calculates various statistics for the student.
    """
    # Get the entry code from the session
    entry_code = request.session.get("entry_code")

    # Retrieve the student based on the entry code
    student = get_object_or_404(Student, entry_code=entry_code)

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
        entry["total_score"] = entry["continuous_assessment_total"] + entry["exam_total"]

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
    for key, group in groupby(student_assessment_scores, key=lambda x: (x.grade_level, x.subject)):
        grade_level, subject = key
        assessment_scores_by_grade_subject.setdefault(grade_level, {}).setdefault(subject, []).extend(group)

    # Get the Subject with the highest total score
    highest_subject = assessment_scores_by_grade_subject
    if highest_subject:
        highest_subject = max(
            subject_totals,
            key=lambda subject: subject["total_score"],
        )
        highest_subject["subject_field"] = Subject.objects.get(name=highest_subject["subject__name"]).subject_field
    else:
        highest_subject = None

    # Calculate the average total score for each subject across
    # all grade levels and session terms
    subject_average_scores = (
        assessment_scores.values("subject__name")
        .annotate(avg_total_score=Avg("total_score"))
        .order_by("subject__name")
    )

    # List the top 3 subjects based on the highest scores (exclude "General")
    top_subjects = (
        AssessmentScore.objects.filter(student=student)
        .exclude(subject__subject_field__name="General")
        .values("subject__name")
        .annotate(total_score=Sum("continuous_assessment") + Sum("exam"))
        .order_by("-total_score")[:3]
    )

    # Get the Subject field of these subjects
    subject_fields_of_top_subjects = [
        Subject.objects.get(name=subj["subject__name"]).subject_field for subj in top_subjects
    ]

    # Calculate the most common subject field if top_subjects is not empty
    most_common_subject_field = None
    if subject_fields_of_top_subjects:
        most_common_subject_field = max(set(subject_fields_of_top_subjects), key=subject_fields_of_top_subjects.count)

    # List the related disciplines based on suggested Subject field
    related_disciplines = Discipline.objects.filter(subject_field=most_common_subject_field)

    template = "assessment.html"
    context = {
        "student": student,
        "assessment_scores": assessment_scores,
        "assessment_scores_by_grade_subject": assessment_scores_by_grade_subject,
        "subject_totals": subject_totals,
        "highest_subject": highest_subject,
        "subject_average_scores": subject_average_scores,
        "top_subjects": top_subjects,
        "most_common_subject_field": most_common_subject_field,
        "related_disciplines": related_disciplines,
    }

    return render(request, template, context)
