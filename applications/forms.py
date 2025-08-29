from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm): #fields are auto generated
    class Meta:
        model = Application
        fields = ["company","job_title","application_link","status","date_applied","notes"]
        widgets = {
            "date_applied": forms.DateInput(attrs={"type":"date"}),
            "notes": forms.Textarea(attrs={"rows":4}),
        }