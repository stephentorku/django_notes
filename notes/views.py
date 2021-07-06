from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect

from .models import Note
# Create your views here.

class NewNoteForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'input-text', 'placeholder': 'Title'}))
    note = forms.CharField(label="", widget=forms.Textarea(attrs={'rows':6, 'class':'input-textarea', 'placeholder': 'Body'}))
    class Meta:
        model = Note
        fields =['title', 'note',]

def all_notes(request):
    return render(request, 'notes/index.html', {'notes': Note.objects.all()})

def add_note(request):
    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'notes/add_note.html', {'form': NewNoteForm()})

def view_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, 'notes/note.html', {'note': note})

def delete_note(request, note_id):
    task = Note.objects.get(pk=note_id)
    if request.method == 'GET':
        task.delete()
        return redirect('/')

def edit_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    # initial={'title': note.title,'note': note.note}
    form = NewNoteForm(instance=note)
    if request.method == 'POST':
        form = NewNoteForm(request.POST, instance = note)
        if form.is_valid():
            title = form.cleaned_data['title']
            note = form.cleaned_data['note']
            form.save()
            return redirect('/')
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note })
    
