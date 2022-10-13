from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Bullscows
from .utils import request_value_handler, creating_new_game, get_game
from django.contrib.auth.models import User



def index(request):
    return render(request, 'game/index.html')


def bullscows(request):
    player = request.user
    if not player.is_authenticated:
        return redirect('/users/login_user/')
    if player.game.count() == 0:
        return render(request, 'game/bullscows.html', context=creating_new_game(player))
    game = get_game(player)
    request_value = request.POST.get('value')
    data = request_value_handler(game=game, request_value=request_value)

    return render(request, 'game/bullscows.html', context=data)

# answer = create_answer()
        #
        # game = Bullscows.objects.create(answer=answer, user=player)
        # game.save()
        # new_game = 'Новая игра'
        # return render(request, 'game/bullscows.html', context={'new_game': new_game})
    # """creating a new gamepage with unique game instance  for user, including answer number"""
    # game = player.game.all()[0]
    # data = {}
    #
    # print(game.answer)
    # if request.method == 'POST':
    #
    #     """part for give-up player's decision"""
    #     if request.POST.get('value') == 'give up':
    #         print('3')
    #         answer = f'Загаданное число - {game.answer}'
    #         list_of_tries = game.try_string.split(',')
    #         game.delete()
    #         return render(request, 'game/bullscows.html', context={'answer': answer, 'list_of_tries': list_of_tries})
    #
    #
    #     elif request.POST.get('value') == 'new game':
    #
    #         new_game = 'Новая игра'
    #         game.delete()
    #         answer = create_answer()
    #
    #         game = Bullscows.objects.create(answer=answer, user=player)
    #         game.save()
    #         return render(request, 'game/bullscows.html', context={'new_game': new_game})
    #
    #     else:
    #         player_try = request.POST.get('value')
    #         if not verify_try(player_try):
    #             list_of_tries = game.try_string.split(',')
    #             warning = "Число должно содержать 4 неповторяющиеся цифры в диапазоне 1-9"
    #             return render(request, 'game/bullscows.html', context={'warning': warning,
    #                                                                     'list_of_tries': list_of_tries})
    #         game.try_string = get_try_string(game.answer, player_try, game.try_string)
    #         game.save()
    #         data['list_of_tries'] = game.try_string.split(',')
    #         tuple_cowsbulls = check_try(game.answer, player_try)
    #         if tuple_cowsbulls[1] == '4':
    #             data['answer'] = f"Вы вычислили загаданное число - {game.answer}. Поздравляем"
    #             game.delete()
