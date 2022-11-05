import pytest
from django.contrib.auth.models import User

from game.utils import creating_new_game, verify_try


@pytest.fixture()
def creating_user(db):
    user = User.objects.create_user("test-user")
    game = creating_new_game(user)
    print("a")
    return {"user": user, "game": game}


@pytest.mark.django_db
def testing_creating_new_game(creating_user):
    assert creating_user["user"].game.count() == 1


@pytest.mark.django_db
def testing_creating_new_game_try_string(creating_user):
    assert creating_user['game'].try_string == ''


@pytest.mark.django_db
def testing_creating_new_game_game_answer(creating_user):
    assert verify_try(creating_user['game'].answer) is True
