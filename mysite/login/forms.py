from .models import Sign_in
from django import forms


class Sign_inForm(forms.ModelForm):
    class Meta:
        model = Sign_in()
        fields = '__all__'
