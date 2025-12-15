from django.urls import reverse_lazy
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    model = Student
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['enrollment_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:list')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
