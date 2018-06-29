from content.models import PrePosting
from django.forms import ModelForm
from django.contrib.admin import widgets
from django import forms

class PostingForm(ModelForm):
    class Meta:
        model = PrePosting
        fields = ('position_title' , 'client_name' , 'date', 'position_city',  'position_description', 'position_link','posted_by' , 'legal_field', 'accept_terms', 'states')
        widgets = {
            'position_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': True, }),
            'client_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': True, }),
            'date': forms.SelectDateWidget(
                 attrs={'class': 'form-control', 'placeholder': '', 'required': True, 'widget': widgets.AdminDateWidget}),

            'position_city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': True, }),

            'position_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': '', 'required': True, }),
            'position_link': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': ' ', 'required': False, }),
            'posted_by': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': False, }),
            'legal_field': forms.CheckboxSelectMultiple(
                attrs={'list-style-type': None, 'required': False, }),
            'accept_terms': forms.CheckboxInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': True, }),
            'states': forms.Select(
                attrs={'class': 'form-control', 'list-style-type': None, 'required': False, })
        }
