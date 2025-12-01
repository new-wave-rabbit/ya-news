# test_routes.py
import pytest
from pytest_django.asserts import assertRedirects
from pytest_lazy_fixtures import lf

from http import HTTPStatus

from django.urls import reverse

@pytest.mark.parametrize(
    "name,args",
    [
        ("news:home", None),
        ("news:detail", pytest.lazy_fixture("news"),),
        ("users:login", None),
        ("users:signup", None),
    ]
)
def test_pages_availability(client, news, name, args):
    # если не используешь lazy_fixture, можно так:
    if name == "news:detail":
        args = (args.id,)
    url = reverse(name, args=args)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
