from django.test import TestCase
from .forms import ContactForm


class ContactFormTestCase(TestCase):

    def test_form_renders_contact_name_input(self):
        form = ContactForm()
        self.assertIn('Full Name', form.as_p())

    def test_form_renders_contact_email_input(self):
        form = ContactForm()
        self.assertIn('Email Address', form.as_p())

    def test_form_renders_contact_message_input(self):
        form = ContactForm()
        self.assertIn('Your Message', form.as_p())

    def test_form_validation_for_blank_contact_name(self):
        form = ContactForm(data={
            'contact_name': '',
            'contact_email': 'test@email.com',
            'contact_message': 'Test Message'})
        self.assertFalse(form.is_valid())

    def test_form_validation_for_blank_contact_email(self):
        form = ContactForm(data={
            'contact_name': 'Test Name',
            'contact_email': '',
            'contact_message': 'Test Message'})
        self.assertFalse(form.is_valid())

    def test_form_validation_for_blank_contact_message(self):
        form = ContactForm(data={
            'contact_name': 'Test Name',
            'contact_email': 'test@email.com',
            'contact_message': ''})
        self.assertFalse(form.is_valid())

    def test_form_validation_for_valid_data(self):
        form = ContactForm(data={
            'contact_name': 'Test Name',
            'contact_email': 'test@email.com',
            'contact_message': 'Test Message'})
        self.assertTrue(form.is_valid())
