from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Rooms, fields
  

class UploadFileForm(forms.Form):
    name = forms.CharField()
    File_field = forms.FileField()
    
class UpdateForm(ModelForm):
    class Meta:
        Model = Rooms
        fields = '__all__'