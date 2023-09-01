from django import forms
from .models import BioData, Location, Contact
class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        # Apply the 'is-invalid' class to the widget's attrs for fields you want to style
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control is-invalid'})

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['country', 'state', 'town', 'zip_code']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        
        # Apply the 'is-invalid' class to the widget's attrs for fields you want to style
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control is-invalid'})

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['phone_number', 'phone_number2', 'email']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        
        # Apply the 'is-invalid' class to the widget's attrs for fields you want to style
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control is-invalid'})
        
      