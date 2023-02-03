from django.test import TestCase
from .models import Contact


class ContactModelTestCase(TestCase):
    def test_contact_model_fields(self):
        """
        Test if the fields on the Contact model are defined correctly
        """
        contact = Contact.objects.create(
            contact_name='Test User',
            contact_email='testuser@example.com',
            contact_message='Test Message'
        )
        self.assertEqual(contact.contact_name, 'Test User')
        self.assertEqual(contact.contact_email, 'testuser@example.com')
        self.assertEqual(contact.contact_message, 'Test Message')

    def test_contact_model_string_representation(self):
        """
        Test the string representation of the Contact model
        """
        contact = Contact.objects.create(contact_name='Test User')
        self.assertEqual(str(contact), 'Test User')
