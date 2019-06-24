from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("movies", views.MoviesList.as_view(), name="MoviesList"),
    path("movie/<int:pk>", views.MovieDetail.as_view(), name="MovieDetail"),
  ]