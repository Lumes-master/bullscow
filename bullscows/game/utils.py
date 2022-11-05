"""Functions for game logic """
from random import sample

from django.contrib.auth.models import User

from .models import Bullscows


def create_answer() -> str:
    """create 4number answer with different digits. Used in
    "creating_new_game" function """
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    answer = ''.join(sample(number_list, 4))
    return answer


def verify_try(player_try: str) -> bool:
    """Validating player try-number Used in "game logic" function """
    if len(player_try) == 4 and len(set(player_try)) == 4:
        for i in player_try:
            if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return False
        return True
    return False


def check_try(answer: str, player_try: str) -> tuple:
    """compares players_try and answer, returns 2 digits -
    number of good guessed digits and number of them on
    the proper place. Used in 'game_logic' function """
    bulls = 0
    cows = 0
    for i in range(len(player_try)):
        if player_try[i] == answer[i]:
            cows += 1
            bulls += 1
        elif player_try[i] in answer:
            cows += 1
    return str(cows), str(bulls)


def get_try_string(answer: str, player_try: str, try_string: str = None) -> str:
    """Creates string, containing of player's try and its result.
    Rerurned as one string to front-end in 'game_logic' function"""
    tuple_cowsbulls = check_try(answer, player_try)
    if not try_string:
        try_string = f'{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
        return try_string
    else:
        try_string += f',{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
    return try_string


def creating_new_game(player: User):
    """Creates game imstance binded to current user. """

    answer = create_answer()

    game = Bullscows.objects.create(answer=answer, user=player)
    game.save()
    return game



def check_answer_is_available(game_answer: str) -> str:
    """Check, if its a start of new game(in that case answer is
    "None". If so - creates new game.answer). Used in "get_game" function"""
    if game_answer == "None":
        answer = create_answer()
        return answer


def get_game(player: User) -> Bullscows:
    """Gets singleton game.instance from db"""
    game = player.game.all()[0]
    answer = check_answer_is_available(game.answer)
    if answer:
        game.answer = answer
    game.save()
    return game



def give_up(game: Bullscows) -> dict:
    """Used in 'request_value_handler'. """
    answer = f'Загаданное число - {game.answer}'
    list_of_tries = game.try_string.split(',')
    data = {"list_of_tries": list_of_tries, "answer": answer}
    game.answer = "None"
    game.try_string = ""
    game.save()
    return data


def new_game(game: Bullscows) -> dict:
    data = {"new_game": 'Новая игра'}
    game.answer = "None"
    game.try_string = ""
    game.save()
    return data


def game_logic(game: Bullscows, request_value: str) -> dict:
    player_try = request_value
    if not verify_try(player_try):
        data = {
            'list_of_tries': game.try_string.split(','),
            "warning": "Число должно содержать 4 неповторяющиеся цифры в диапазоне 1-9"}
        return data
    game.try_string = get_try_string(game.answer, player_try, game.try_string)
    game.save()
    data = {'list_of_tries': game.try_string.split(',')}
    tuple_cowsbulls = check_try(game.answer, player_try)
    if tuple_cowsbulls[1] == '4':
        data['answer'] = f"Вы вычислили загаданное число - {game.answer}. Поздравляем"
        game.try_string = ""
        game.answer = "None"
        game.save()
    return data


def request_value_handler(game: Bullscows, request_value: str) -> dict:
    if request_value == 'give up':
        return give_up(game)
    elif request_value == 'new game':
        return new_game(game)
    elif request_value is None:
        data = {'list_of_tries': game.try_string.split(',')}
        return data
    else:
        return game_logic(game, request_value)





