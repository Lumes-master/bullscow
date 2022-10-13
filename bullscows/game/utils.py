"""Functions for game logic """
from random import sample

from django.contrib.auth.models import User

from .models import Bullscows


def create_answer() -> str:
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    answer = ''.join(sample(number_list, 4))
    return answer


def verify_try(player_try: str) -> bool:
    if len(player_try) == 4 and len(set(player_try)) == 4:
        for i in player_try:
            if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return False
        return True
    return False


def check_try(answer: str, player_try: str) -> tuple:
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
    tuple_cowsbulls = check_try(answer, player_try)
    if not try_string:
        try_string = f'{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
        return try_string
    else:
        try_string += f',{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
    return try_string


def creating_new_game(player: User):
    if player.game.count() == 0:
        answer = create_answer()

        game = Bullscows.objects.create(answer=answer, user=player)
        game.save()
        data = {"new_game": 'Новая игра'}
        return data


def check_answer_is_available(game_answer: str) -> str:
    if game_answer == "None":
        answer = create_answer()
        return answer


def get_game(player: User) -> Bullscows:
    game = player.game.all()[0]
    answer = check_answer_is_available(game.answer)
    if answer:
        game.answer = answer
    game.save()
    return game


"""creating a new gamepage with unique game instance  for user, including answer number"""


def give_up(game: Bullscows) -> dict:
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
        game.answer = "None"
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





# if __name__ == '__main__':
#     a = create_answer()
#     print(a)
    # try_string = ""
    # player_try = "5678"
    # try_string= get_try_string(a, player_try, try_string)
    # print(try_string)
    # player_try1 = "3456"
    # try_string = get_try_string(a, player_try1, try_string)
    # print(try_string)
    # try_list = try_string.split(',')
    # print(try_list)
    # user = User.objects.get(id==1)
    # print(user)
