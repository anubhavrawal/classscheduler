from django import forms
from django.forms import ModelForm
from .models import Rooms, fields


class UploadFileForm(forms.Form):
    term_Name = forms.CharField(
        required=True, strip=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Fall_2021'}
        )
    )
    dept_Name = forms.CharField(
        required=True, strip=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'CS'}
        )
    )
    input_file = forms.FileField(
        allow_empty_file=False, label='',
        widget=forms.ClearableFileInput(
            attrs={'class': 'form-control-file', 'type': 'file'}
        )
    )


class UpdateForm(ModelForm):
    class Meta:
        Model = Rooms
        fields = '__all__'
