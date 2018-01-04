from django import forms

class form(forms.Form):
    vms = forms.ChoiceField(widget=forms.Select(), required=True)