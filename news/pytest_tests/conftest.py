# conftest.py
import pytest

# Импортируем класс клиента.
from django.test.client import Client

# Импортируем модель заметки, чтобы создать экземпляр.
from news.models import Comment, News
from django.contrib.auth import get_user_model
User = get_user_model()


@pytest.fixture
def author(db):
    return User.objects.create(username="Лев Толстой")


@pytest.fixture
def reader(db):
    return User.objects.create(username="Читатель простой")


@pytest.fixture
def news(db):
    return News.objects.create(title="Заголовок", text="Текст")


@pytest.fixture
def comment(db, news, author):
    return Comment.objects.create(
        news=news,
        author=author,
        text="Текст комментария"
    )



# @pytest.fixture
# # Используем встроенную фикстуру для модели пользователей django_user_model.
# def author(django_user_model):
#     return django_user_model.objects.create(username='Автор')


# @pytest.fixture
# def not_author(django_user_model):  
#     return django_user_model.objects.create(username='Не автор')


@pytest.fixture
def author_client(author):  # Вызываем фикстуру автора.
    # Создаём новый экземпляр клиента, чтобы не менять глобальный.
    client = Client()
    client.force_login(author)  # Логиним автора в клиенте.
    return client


@pytest.fixture
def reader_client(reader):
    client = Client()
    client.force_login(reader)  # Логиним обычного пользователя в клиенте.
    return client


# @pytest.fixture
# def news():
#     news = News.objects.create(title='Заголовок', text='Текст')
#     return news

# @pytest.fixture
# def comment(author):
#     comment = Comment.objects.create(
#             news=news(author),
#             author=author,
#             text='Текст комментария'
#         )
#     return comment


# @pytest.fixture
# # Фикстура запрашивает другую фикстуру создания заметки.
# def slug_for_args(note):  
#     # И возвращает кортеж, который содержит slug заметки.
#     # На то, что это кортеж, указывает запятая в конце выражения.
#     return (note.slug,) 