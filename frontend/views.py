import logging

from django.views.generic import TemplateView, ListView, FormView
from django.utils.decorators import method_decorator
from django.http import HttpResponseServerError

from django_ratelimit.decorators import ratelimit

from snippets.models import Snippet
from polls.models import Question
from notes.models import Notes
from weather.forms import WeatherForm
from weather.services import get_weather


logger = logging.getLogger(__name__)


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


@method_decorator(ratelimit(key="ip", rate="5/m", block=True), name="dispatch")
class WeatherRequestView(FormView):
    template_name = "frontend/weather_form.html"
    form_class = WeatherForm

    def form_valid(self, form):
        data = form.cleaned_data
        weather = get_weather(data)
        if not weather:
            return HttpResponseServerError("Server error")

        self.request.session["weather"] = weather
        return self.render_to_response(
            self.get_context_data(form=form, weather=weather)
        )
