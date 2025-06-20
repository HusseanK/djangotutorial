from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path("", include("frontend.urls"), name= "home" ),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("notes/", include("notes.urls")),
    path("Users/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("snippets/", include("snippets.urls")),
]
