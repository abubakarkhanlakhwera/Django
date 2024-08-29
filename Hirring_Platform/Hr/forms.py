from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import HRProfile

from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'salary']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'salary': forms.NumberInput(attrs={'step': '0.01'}),
        }


class HRSignupForm(UserCreationForm):
    company_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'company_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            hr_profile = HRProfile.objects.create(user=user, company_name=self.cleaned_data['company_name'])
        return user
