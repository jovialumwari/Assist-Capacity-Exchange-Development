from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['description', 'bug_type', 'report_date', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'bug_type': forms.TextInput(attrs={'class': 'form-control'}),
            'report_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
