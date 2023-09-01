
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BioDataForm, LocationForm, ContactForm

# Create your views here.
def form(request):
    if request.method == 'POST':
        biodata_form = BioDataForm(request.POST, prefix='biodata')
        location_form = LocationForm(request.POST, prefix='location')
        contact_form = ContactForm(request.POST, prefix='contact')
        print(request.POST)
        if biodata_form.is_valid() and location_form.is_valid() and contact_form.is_valid():
            biodata = biodata_form.save()
            location = location_form.save()
            contact = contact_form.save()
           
            # You can perform additional actions here
            return redirect('form')  # Redirect to a success page

    else:
        biodata_form = BioDataForm(prefix='biodata')
        location_form = LocationForm(prefix='location')
        contact_form = ContactForm(prefix='contact')

    return render(request, 'form.html', {
        'biodata_form': biodata_form,
        'location_form': location_form,
        'contact_form': contact_form,
    })

def success(request):
    return render(request,'form.html')