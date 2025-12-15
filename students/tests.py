from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Student


class StudentCrudTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            enrollment_date=date(2024, 1, 1),
            active=True,
        )

    def test_list_view(self):
        resp = self.client.get(reverse('students:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'John')

    def test_create_view(self):
        payload = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane@example.com',
            'enrollment_date': '2024-02-01',
            'active': True,
        }
        resp = self.client.post(reverse('students:create'), payload, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Student.objects.filter(email='jane@example.com').exists())

    def test_update_view(self):
        payload = {
            'first_name': 'Johnny',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'enrollment_date': '2024-01-01',
            'active': False,
        }
        resp = self.client.post(reverse('students:edit', args=[self.student.id]), payload, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Johnny')
        self.assertFalse(self.student.active)

    def test_delete_view(self):
        resp = self.client.post(reverse('students:delete', args=[self.student.id]), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())
