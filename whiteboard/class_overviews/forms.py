from django import forms
from .models import Course, Section, Document

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    file = forms.FileField(label='Select a file')

    '''name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    path = forms.CharField(max_length=254)
    #file = forms.FileField()

    def add_document(self, request):
        section = Section.objects.filter(section_number = 8750)[0]
        doc = Document(self.name, self.description, self.path, section)
        doc.save()'''