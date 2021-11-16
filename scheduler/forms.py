from django import forms
  
class UploadFileForm(forms.Form):
    name = forms.CharField()
    File_field = forms.FileField()