from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from core.models import Movie
from core.views import MoviesList

# Create your tests here.

class MovieListPaginationTestCase(TestCase):

    ACTIVE_PAGINATION_HTML = """
    <li class="page-item active">
        <a class="page-link" href="{}?page={}">
            {}
        </a>
    </li>
    """

    def setUp(self) -> None:
        for n in range(15):
            Movie.objects.create(
                title=f"Title {n}",
                year=1990+n,
                runtime=100
            )

    def testFirstPage(self):
        movie_list_url = reverse("core:MoviesList")
        request = RequestFactory().get(path=movie_list_url)
        responce = MoviesList.as_view()(request)

        self.assertEqual(200, responce.status_code)
        self.assertTrue(responce.context_data["is_paginated"])
        self.assertInHTML(
            self.ACTIVE_PAGINATION_HTML.format(movie_list_url, 1, 1),
            responce.rendered_content
        )
