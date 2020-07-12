from django.shortcuts import render
from django.utils import timezone
from .models import Note


def notes_list(request):
	notes = Note.objects.filter(date__lte=timezone.now()).order_by('date') 
	return render(request, 'notes/notes_list.html', {'notes': notes})
