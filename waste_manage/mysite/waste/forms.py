from django import forms
from .models import Issue


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = ['issue_place','issue_desc','issue_period','issue_image']
