from django import forms

class WeatherForm(forms.Form):
    city = forms.CharField()
    country = forms.CharField(widget=forms.Textarea)
    timeframe = forms.SplitDateTimeWidget()

    def confirm_details(self):
        pass



