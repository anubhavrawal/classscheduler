from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Rooms, fields


class UploadFileForm(forms.Form):
    input_file = forms.FileField(allow_empty_file=False, label='', widget=forms.ClearableFileInput(
        attrs={'class': 'form-control-file', 'type': 'file'}))


class UpdateForm(ModelForm):
    class Meta:
        Model = Rooms
        fields = '__all__'
