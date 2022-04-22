from dataclasses import fields
from re import A
from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
	class Meta:
		model = Diary
		fields = ('date', 'title', 'text',)
		widgets = {
			'date': forms.DateInput(attrs={'class': 'form-control'}),
			'title': forms.DateInput(attrs={'class': 'form-control'}),
			'text': forms.DateInput(attrs={'class': 'form-control'}),
		}