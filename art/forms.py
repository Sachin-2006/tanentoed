from django import forms
from .models import ArtSave
from userauth.models import *
class ArtForm(forms.ModelForm):
	class Meta:
		model = ArtSave
		fields = ['file','description']
 