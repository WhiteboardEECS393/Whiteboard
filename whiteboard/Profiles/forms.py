from django import forms
from .models import StudentUser, Major, Minor
from class_overviews.models import Section, Semester
from django.shortcuts import HttpResponse


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email_id = forms.EmailField(max_length=254)
    bio = forms.CharField(max_length=500)
    grad_year = forms.IntegerField()
    majors = forms.ModelMultipleChoiceField(queryset=Major.objects.all(), widget=forms.SelectMultiple, required=False)
    minors = forms.ModelMultipleChoiceField(queryset=Minor.objects.all(), widget=forms.SelectMultiple, required=False)
    semester = Semester(season = "Fall", year = 2015, startDate = 2015-8-24, endDate = 2015-12-4)
    curr_classes = forms.ModelMultipleChoiceField(queryset=Section.objects.filter(semester = semester), widget=forms.SelectMultiple, required=False)


    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email_id = self.cleaned_data.get('email_id')
        bio = self.cleaned_data.get('bio')
        grad_year = self.cleaned_data.get('grad_year')
        majors = self.cleaned_data.get('majors')
        minors = self.cleaned_data.get('minors')
        curr_classes = self.cleaned_data.get('curr_classes')
        return self.cleaned_data

    def edit_user(self, request):
        current_user = StudentUser.objects.filter(user=request.user)[0]
        current_user.first_name = self.cleaned_data.get('first_name')
        current_user.last_name = self.cleaned_data.get('last_name')
        current_user.email_id = self.cleaned_data.get('email_id')
        current_user.bio = self.cleaned_data.get('bio')
        current_user.grad_year = self.cleaned_data.get('grad_year')
        current_user.majors = self.cleaned_data.get('majors')
        current_user.minors = self.cleaned_data.get('minors')
        semester = Semester(season = "Fall", year = 2015, startDate = 2015-8-24, endDate = 2015-12-4)
        current_user.student_classes.remove(*(current_user.student_classes.filter(semester = semester)))
        current_user.student_classes.add(*(self.cleaned_data.get('curr_classes')))
        current_user.save()

class EditProfilePictureForm(forms.Form):
    file = forms.FileField(label='Select a file')
