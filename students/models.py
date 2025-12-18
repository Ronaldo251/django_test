from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome do Curso")
    created_at = models.DateField(verbose_name="Data de Criação")

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Primeiro Nome")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome")
    email = models.EmailField(unique=True, verbose_name="E-mail")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Aluno")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name="Curso")
    
    enrollment_date = models.DateField(verbose_name="Data da Matrícula")
    active = models.BooleanField(default=True, verbose_name="Ativo")
    
    is_free = models.BooleanField(default=False, verbose_name="Gratuito")

    class Meta:
        unique_together = ('student', 'course') 

    def __str__(self):
        return f"{self.student} - {self.course}"

    def save(self, *args, **kwargs):
        if self.student.first_name.upper().startswith('A'):
            self.is_free = True
        else:
            self.is_free = False
            
        super().save(*args, **kwargs)