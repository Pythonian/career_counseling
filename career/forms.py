from django import forms

from .models import Student


class AccessForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["entry_code"]

    def clean_entry_code(self):
        entry_code = self.cleaned_data.get("entry_code")
        if not Student.objects.get(entry_code=entry_code).exists():
            raise forms.ValidationError("Invalid code")
        return entry_code
