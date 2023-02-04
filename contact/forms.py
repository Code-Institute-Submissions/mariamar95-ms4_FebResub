from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_email', 'contact_message']

    def __init__(self, *args, **kwargs):
        """
        Add Placeholders
        Remove Labels
        Add aria-labels
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'contact_name': 'Full Name',
            'contact_email': 'Email Address',
            'contact_message': 'Your Message',
        }
        self.fields['contact_name'].widget.attrs['autofocus'] = True
        self.fields['contact_name'].widget.attrs['aria-label'] = 'Name'
        self.fields['contact_email'].widget.attrs['aria-label'] = 'Email'
        self.fields['contact_message'].widget.attrs[
            'aria-label'] = 'Your message'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
