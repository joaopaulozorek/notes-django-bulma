from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import NoteForm
from .models import Note


def note_list(request):
	notes = Note.objects.filter(date__lte=timezone.now()).order_by('date') 
	return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk):
	note = get_object_or_404(Note, pk=pk)
	return render(request, 'notes/note_detail.html', {'note': note})

def note_new(request):
	if request.method == "POST":
		form = NoteForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.author = request.user
			note.date = timezone.now()
			note.save()
			return redirect('note_detail', pk=note.pk)
	else:
		form = NoteForm()
	return render(request, 'notes/note_edit.html', {'form': form})

def note_edit(request, pk):
	note = get_object_or_404(Note, pk=pk)
	if request.method == "POST":
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			note = form.save(commit=False)
			note.author = request.user
			note.date = timezone.now()
			note.save()
			return redirect('note_detail', pk=note.pk)
	else:
		form = NoteForm(instance=note)
	return render(request, 'notes/note_edit.html', {'form': form})

def note_remove(request, pk):
	note = get_object_or_404(Note, pk=pk)
	note.delete()
	return redirect('note_list')