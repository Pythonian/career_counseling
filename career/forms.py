from django import forms

from .models import Student


class AccessForm(forms.Form):
    entry_code = forms.CharField(
        label="",
        max_length=10,
        widget=forms.TextInput(
            attrs={"placeholder": "Enter access code", "class": "form-control"}
        ),
    )

    def clean_entry_code(self):
        entry_code = self.cleaned_data.get("entry_code")
        try:
            Student.objects.get(entry_code=entry_code)
        except Student.DoesNotExist:
            raise forms.ValidationError("Invalid code")
        return entry_code
