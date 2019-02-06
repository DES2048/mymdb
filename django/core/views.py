from django.shortcuts import render
from django.views.generic import ListView, DetailView # автоклассы жанги для списочного и детального отображения

from core.models import Movie


# Create your views here.
class MoviesList(ListView):
    # этот атрибут класса говорит данные какой модкли мы будем использовать для списка
    model = Movie


class MovieDetail(DetailView):
    model = Movie
