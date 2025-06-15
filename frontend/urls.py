from django.urls import path, include

from frontend import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name= "home"),
    path("snippets/", views.SnippetsPageView.as_view(), name= "snippets"),
    path("polls/", views.PollsPageView.as_view(), name= "polls"),
    path("notes/", views.NotesPageView.as_view(), name= "notes"),
    path("weather/", views.WeatherRequestView.as_view(), name= "weather"),
    # path("weather/detail/", views.WeatherView.as_view(), name= "weather-detail"),
]
