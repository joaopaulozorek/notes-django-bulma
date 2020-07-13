from django import forms
from .models import Note

class NoteForm(forms.ModelForm):

	class Meta:
		model = Note
		fields = ('title', 'text',)

	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class': 'input is-medium', 'placeholder':'Large input'})