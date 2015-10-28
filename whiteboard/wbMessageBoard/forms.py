from django import forms


class BoardForm(forms.Form):
    thread_name = forms.CharField(label='Thread Name', max_length=200)
    thread_description = forms.CharField(label='Thread Description', max_length=300)


class ThreadForm(forms.Form):
    thread_subject = forms.CharField(label='Subject', max_length=200)
    thread_message = forms.CharField(label='Message', max_length=1000)


class ReplyForm(forms.Form):
    reply_message = forms.CharField(label='Message', max_length=1000)
