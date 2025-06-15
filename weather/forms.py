from django import forms

class WeatherForm(forms.Form):
    state = forms.CharField()
    country = forms.CharField()
    date_from = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))