from django.db import models
from django.utils import timezone
from django.urls import reverse


class Notes(models.Model):
    description = models.CharField(max_length=50)
    content = models.TextField(default="")
    date_created = models.DateTimeField(default=timezone.datetime.now)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("notes:notes-detail", kwargs={"pk": self.pk})
