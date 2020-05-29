from django import forms
from .models import Contact
from .models import Notes


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'birthday',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
        ]

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [
            'note',

        ]