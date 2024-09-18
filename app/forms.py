from django import forms
from . models import Invoice

class InvoiceCreateForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['amount', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
