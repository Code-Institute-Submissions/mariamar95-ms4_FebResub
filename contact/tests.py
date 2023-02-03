from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import ContactForm


class ContactViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')
        self.user = User.objects.create_user(
            username='testuser', password='secret')

    def test_contact_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_view_redirects_to_success_template_on_valid_post(self):
        data = {'contact_name': 'Test User', 'contact_email': 'test@example.com', 'contact_message': 'Test Message'}
        response = self.client.post(self.url, data)
        self.assertRedirects(response, reverse('success'))

    def test_contact_view_displays_error_on_invalid_post(self):
        data = {'contact_name': '', 'contact_email': '', 'contact_message': ''}
        response = self.client.post(self.url, data)
        self.assertContains(response, 'Your message was not sent.')
