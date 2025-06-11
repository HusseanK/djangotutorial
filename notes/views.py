from django.shortcuts import render
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .models import Notes


class NoteView(ListView):
    model = Notes
    template_name = "notes/notes_home.html"
    context_object_name = "notes"
    ordering = ["-date_created"]
    paginate_by = 10


class NoteCreate(CreateView):
    model = Notes
    template_name = "notes/notes_create.html"
    fields = ["description", "content"]


class NoteDetailView(DetailView):
    model = Notes
    template_name = "notes/notes_detail.html"


class NoteUpdateView(UpdateView):
    model = Notes
    fields = ["description", "content"]
    template_name = "notes/update.html"
    success_url = reverse_lazy("notes:notes")


class NoteDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy("notes:notes")
    template_name = "notes/delete.html"
