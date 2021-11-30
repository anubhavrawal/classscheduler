from django import forms
from django.forms import ModelForm
from .models import Rooms, fields
  

class UploadFileForm(forms.Form):
    name = forms.CharField()
    dept = forms.CharField()
    file_field = forms.FileField()


class UpdateForm(ModelForm):
    class Meta:
        Model = Rooms
        fields = '__all__'