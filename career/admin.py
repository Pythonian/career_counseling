from django.contrib import admin
from django.core.mail import send_mail
from django.contrib.auth.models import Group

from career.models import (
    AssessmentScore,
    Discipline,
    GradeLevel,
    SessionTerm,
    Student,
    Subject,
    SubjectField,
)


class AssessmentScoreInline(admin.TabularInline):
    model = AssessmentScore


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [AssessmentScoreInline]
    list_display = ["name", "entry_code", "email"]

    def save_model(self, request, obj, form, change):
        if not change:  # Check if the student object is being created
            entry_code = obj.entry_code

            # Your email sending logic here
            subject = 'Your Entry Code'
            message = f'Hello {obj.name},\n\nYour entry code is: {entry_code}\n\nPlease keep this code safe and use it for future references.\n\nBest regards,\nYour School Team'
            from_email = 'school@example.com'  # Replace this with your desired sender email
            recipient_list = [obj.email]

            send_mail(subject, message, from_email, recipient_list)

        super().save_model(request, obj, form, change)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "subject_field"]
    list_filter = ["subject_field"]


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ["name", "subject_field"]


admin.site.register(SubjectField)
admin.site.register(GradeLevel)
admin.site.register(SessionTerm)
admin.site.unregister(Group)