from django import forms

from webapp.models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model: Quote
        fields = ('text', 'name', 'email')

