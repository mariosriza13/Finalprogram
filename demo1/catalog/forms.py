from django import forms

class ItemSearchForm(forms.Form):
    query = forms.CharField(label='Search', required=False)