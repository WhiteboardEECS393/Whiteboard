from django import forms

class EventForm(forms.Form):
    event_name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=300)
    start = forms.TimeField()
    end = forms.TimeField()
    allDay = forms.BooleanField(required=False)
    start_date = forms.DateField()
    end_date = forms.DateField()
    recurring = forms.BooleanField()
    dow = forms.CharField(max_length=7)