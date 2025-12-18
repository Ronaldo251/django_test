from django import forms
from .models import Student, Enrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course', 'enrollment_date', 'active']
        widgets = {
            'enrollment_date': forms.DateInput(attrs={'type': 'date'})
        }