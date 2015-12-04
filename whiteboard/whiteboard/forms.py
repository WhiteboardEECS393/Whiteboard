from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from Profiles.models import StudentUser, Major, Minor


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Incorrect Username or Password")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirmpass = forms.CharField(widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email_id = forms.EmailField(max_length=254)
    bio = forms.CharField(max_length=500)
    grad_year = forms.IntegerField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirmpass = self.cleaned_data.get('confirmpass')
        if len(User.objects.filter(username=username)) > 0:
            raise forms.ValidationError("Username already taken")
        elif confirmpass != password:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data

    def create_new_user(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email_id = self.cleaned_data.get('email_id')
        bio = self.cleaned_data.get('bio')
        grad_year = self.cleaned_data.get('grad_year')
        User.objects.create_user(username=username, password=password)
        user = authenticate(username=username, password=password)
        new_student = StudentUser(
            user=user,
            first_name=first_name,
            last_name=last_name,
            full_name=first_name + ' ' + last_name,
            email_id=email_id,
            bio=bio,
            grad_year=grad_year,
            )
        new_student.save()
        return user
