from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.urls import reverse_lazy

from rest_framework.response import Response
from rest_framework.decorators import api_view

from snippets.models import Snippet
from polls.models import Question
from notes.models import Notes

from weather.forms import WeatherForm
from weather.services import get_weather

from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit



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


@method_decorator(
    ratelimit(key='ip', rate='5/m', block=True),
    name='dispatch'
)
class WeatherRequestView(FormView):
    template_name = "frontend/weather_form.html"
    form_class = WeatherForm
    # success_url = reverse_lazy("weather-detail") #Temp

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            weather = get_weather(data)
            print(weather)
        except Exception as e:
            print('excepted')
            print(e) #lazy af
        self.request.session['weather'] = weather
        return self.render_to_response(self.get_context_data(form=form, weather=weather))

# class WeatherView(TemplateView):
#     template_name = "frontend/weather_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # weather = self.request.session.pop('weather', None)
#         weather = self.request.session.get('weather')

#         if weather:
#             context['weather'] = weather
#         else:
#             context['error'] = "No Weather data available"
#         return context