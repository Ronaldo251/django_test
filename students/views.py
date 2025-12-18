from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Enrollment, Course
from .forms import StudentForm, EnrollmentForm

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

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')

#visualização lógica no front

class EnrollmentListView(ListView):
    model = Enrollment
    context_object_name = 'enrollments'
    template_name = 'students/enrollment_list.html'