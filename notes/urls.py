from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("", views.NoteView.as_view(), name="notes"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="notes-detail"),
    path("<int:pk>/update/", views.NoteUpdateView.as_view(), name="notes-update"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="notes-delete"),
    path("new/", views.NoteCreate.as_view(), name="create"),
]
