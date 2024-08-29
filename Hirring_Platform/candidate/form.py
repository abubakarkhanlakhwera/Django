from django import forms
from .models import Candidate

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name','email','phone','skills','resume']