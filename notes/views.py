from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Note


def notes_list(request):
	notes = Note.objects.filter(date__lte=timezone.now()).order_by('date') 
	return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
	note = get_object_or_404(Note, pk=pk)
	return render(request, 'notes/note_detail.html', {'note': note})
