from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from snippets.models import Snippet
from polls.models import Question
from notes.models import Notes


class HomePageView(TemplateView):
    template_name = "frontend/home.html"


class PollsPageView(ListView):
    template_name = "frontend/polls.html"
    queryset = Question.objects.all()
    model = Question
    context_object_name = "polls"
    paginate_by = 10

class SnippetsPageView(ListView):
    template_name = "frontend/snippets.html"
    queryset = Snippet.objects.all()
    model = Snippet
    context_object_name = "snippets"
    paginate_by = 10

class NotesPageView(ListView):
    template_name = "frontend/notes.html"
    queryset = Notes.objects.all()
    model = Notes
    context_object_name = "notes"
    paginate_by = 10
