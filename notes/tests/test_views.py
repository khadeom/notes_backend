from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from notes.models import Note

class NoteListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_note_list(self):
        Note.objects.create(title='Test Note', content='This is a test note', owner=self.user)
        response = self.client.get('/api/notes/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        # Add more assertions as needed

    def test_create_note(self):
        # invalid Auth 
        data = {'title': 'New Note', 'content': 'This is a new note'}
        response = self.client.post('/api/notes/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Note.objects.count(), 0)
        # Add more assertions as needed
