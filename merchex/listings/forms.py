from django import forms
from listings.models import Band
from listings.models import Listing


class ContactUsForm(forms.Form):

    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
