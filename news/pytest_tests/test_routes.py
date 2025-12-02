import pytest

from http import HTTPStatus

from django.urls import reverse

from pytest_django.asserts import assertRedirects
from pytest_lazy_fixtures import lf

@pytest.mark.parametrize(
    'name,args',
    [
        ('news:home', None),
        ('news:detail', pytest.lazy_fixture('news'),),
        ('users:login', None),
        ('users:signup', None),
    ]
)
def test_pages_availability(client, name, args):
    if name == 'news:detail':
        args = (args.id,)
    url = reverse(name, args=args)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize(
    'test_comment',
    (pytest.lazy_fixture('comment'),)
)
@pytest.mark.parametrize(
    'name',
    ('news:edit', 'news:delete')
)
@pytest.mark.parametrize(
    'parametrized_client,expected_status',
    (
        (lf('author_client'), HTTPStatus.OK),
        (lf('reader_client'), HTTPStatus.NOT_FOUND),
    )
)
def test_availability_for_comment_edit_and_delete(parametrized_client, name, expected_status, test_comment):
    url = reverse(name, args=(test_comment.id,))
    response = parametrized_client.get(url)
    assert response.status_code == expected_status

@pytest.mark.parametrize(
    'name,c',
    (
        ('news:edit', pytest.lazy_fixture('comment')),
        ('news:delete', pytest.lazy_fixture('comment'))
    )
)
def test_redirect_for_anonymous_client(client, name, c):
    login_url = reverse('users:login')
    url = reverse(name, args=(c.id,))
    redirect_url = f'{login_url}?next={url}'
    response = client.get(url)
    assertRedirects(response, redirect_url)
