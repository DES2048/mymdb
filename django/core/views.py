from django.views.generic import ListView, DetailView # автоклассы жанги для списочного и детального отображения

from core.models import Movie, Person


# Create your views here.
class MoviesList(ListView):
    # этот атрибут класса говорит данные какой модкли мы будем использовать для списка
    model = Movie
    paginate_by = 10


class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_persons()


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()
