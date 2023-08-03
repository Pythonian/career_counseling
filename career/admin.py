from django.contrib import admin

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
    list_display = ["name", "entry_code"]


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
