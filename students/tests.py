from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Student, Course, Enrollment

class StudentTests(TestCase):
    def setUp(self):
        #Criar um curso para testar matriculas
        self.course = Course.objects.create(name="Python Pro", created_at=date.today())
        #Criar aluno que não comece com 'A'
        self.student = Student.objects.create(
            first_name='Joao',
            last_name='Dominicano',
            email='joao@solyd.com'
        )

    # --- TESTES DE VIEWS  ---

    def test_list_view(self):
        resp = self.client.get(reverse('students:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Joao')

    def test_create_student_view(self):
        payload = {
            'first_name': 'Joana',
            'last_name': 'Sebastiana',
            'email': 'joana@solyd.com',
        }
        resp = self.client.post(reverse('students:create'), payload, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Student.objects.filter(email='joana@solyd.com').exists())

    def test_update_student_view(self):
        payload = {
            'first_name': 'Joao',
            'last_name': 'Dominicano',
            'email': 'joao@solyd.com',
        }
        resp = self.client.post(reverse('students:edit', args=[self.student.id]), payload, follow=True)
        self.assertEqual(resp.status_code, 200)
        
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Joao')

    def test_delete_student_view(self):
        resp = self.client.post(reverse('students:delete', args=[self.student.id]), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())


class BusinessLogicTests(TestCase):
    
    def setUp(self):
        self.course = Course.objects.create(name="Django Master", created_at=date.today())

    def test_student_starts_with_A_is_free(self):
        # Criamos aluno com A
        student_a = Student.objects.create(first_name='Ana', last_name='Silva', email='ana@test.com')
        
        # testar a automação sem especificar is_free)
        enrollment = Enrollment.objects.create(
            student=student_a, 
            course=self.course, 
            enrollment_date=date.today()
        )
        
        # Teste se rodou como 'grátis'
        self.assertTrue(enrollment.is_free, "Erro: Aluno com 'A' deveria ter is_free=True")

    def test_student_starts_with_other_letter_is_paid(self):
        # Criamos aluno com B
        student_b = Student.objects.create(first_name='Bruno', last_name='Souza', email='bruno@test.com')
        
        enrollment = Enrollment.objects.create(
            student=student_b, 
            course=self.course, 
            enrollment_date=date.today()
        )
        
        # Verificamos se NÃO é grátis
        self.assertFalse(enrollment.is_free, "Erro: Aluno sem 'A' não deveria ser grátis")

    def test_case_insensitive(self):
        # Teste para reconhecimento de letras minusculas no primeiro nome
        student_lower = Student.objects.create(first_name='arnold', last_name='Schwarzenegger', email='arnold@test.com')
        
        enrollment = Enrollment.objects.create(
            student=student_lower,
            course=self.course,
            enrollment_date=date.today()
        )
        
        self.assertTrue(enrollment.is_free, "Erro: Lógica deve ignorar maiúsculas/minúsculas")