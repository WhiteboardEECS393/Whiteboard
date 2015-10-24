from django import forms


class BoardForm(forms.Form):
    thread_name = forms.CharField(label='Thread Name', max_length=200)
    thread_description = forms.CharField(label='Thread Description', max_length=300)
