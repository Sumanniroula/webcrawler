from django import forms
from .models import Names
from urlparse import urlparse

class PostForm(forms.ModelForm):

    class Meta:
        model = Names
        fields = ('link',)