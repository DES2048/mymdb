from django.db import models


# Модель представляющая Фильм
class Movie(models.Model):
    # Константы возр. рейтинга
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    
    # огр. сисок значений для поля rating
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audiences'),
        (RATED_PG, "PG - Parental Guidance"),
        (RATED_R, "R = Restricted"),
    )
    
    # поля
    # название фильма
    title = models.CharField(max_length=200)
    # описание фильма
    plot = models.TextField(blank=True)
    
    # год выпуска фильма
    year = models.PositiveIntegerField()
    
    # передаем параметр choice, чтобы ограничить список возм. значенийы
    rating = models.IntegerField(choices = RATINGS, default = NOT_RATED)
    
    # длительность в минутах
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    class Meta:
        ordering = ("-year", "title")  # adding base ordering

    director = models.ForeignKey(
        to="Person",
        on_delete=models.SET_NULL,
        related_name="directed",
        null=True,
        blank=True
    )

    writers = models.ManyToManyField(
        to="Person",
        related_name="writing_credits",
        blank=True
    )

    actors = models.ManyToManyField(
        to="Person",
        related_name="acting_credits",
        through="Role",
        blank=True
    )

    def __str__(self):
        return "{} ({})".format(self.title, self.year)


class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True)
    born = models.DateField()
    died = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self):
        if self.died:
            return f"{self.first_name} {self.last_name} ({self.born} - {self.died})"
        else:
            return f"{self.first_name} {self.last_name} ({self.born})"


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=140)

    class Meta:
        unique_together = (
            "movie",
            "person",
            "name",
        )

    def __str__(self):
        return f"{self.movie_id} {self.person_id} {self.name}"
