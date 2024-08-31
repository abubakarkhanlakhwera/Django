from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import HRProfile, Job
from candidate.models import Candidate

# HR Profile Form
class HRProfileForm(forms.ModelForm):
    class Meta:
        model = HRProfile
        fields = ['full_name', 'company_name', 'position_title', 'contact_number', 'email', 'company_website', 'linkedin_profile', 'bio']

# Job Form
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'salary', 'location']

# Job Application Form for Candidate
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['resume', 'cover_letter']  # Assuming these fields exist in Candidate model
