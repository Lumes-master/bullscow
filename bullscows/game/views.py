from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Bullscows
from .utils import create_answer, check_try, verify_try, get_try_string
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    a = request.GET.get('name')
    return render(request, 'game/index.html', {'a': a})


def bullscows(request):
    player = request.user
    print(player)

    """creating a new gamepage  for user"""
    if player.game.count() == 0:
        print('1')
        answer = create_answer()

        game = Bullscows.objects.create(answer=answer, user=player)
        game.save()
        new_game = 'Новая игра'
        return render(request, 'game/bullscows.html', context={'new_game': new_game})

    game = player.game.all()[0]
    data = {}

    print(game.answer)
    if request.method == 'POST':
        print("post")
        """part for give-up player's decision"""
        if request.POST.get('value') == 'give up':
            print('3')
            answer = f'Загаданное число - {game.answer}'
            list_of_tries = game.try_string.split(',')
            game.delete()
            return render(request, 'game/bullscows.html', context={'answer': answer, 'list_of_tries': list_of_tries})
        elif request.POST.get('new game') == 'new game':
            print('new game')
            new_game = 'Новая игра'
            game.delete()
            answer = create_answer()

            game = Bullscows.objects.create(answer=answer, user=player)
            game.save()
            return render(request, 'game/bullscows.html', context={'new_game': new_game})
        else:
            player_try = request.POST.get('name')
            if not verify_try(player_try):
                list_of_tries = game.try_string.split(',')
                warning = "Число должно содержать 4 неповторяющиеся цифры в диапазоне 1-9"
                return render(request, 'game/bullscows.html', context={'warning': warning,
                                                                        'list_of_tries': list_of_tries})
            game.try_string = get_try_string(game.answer, player_try, game.try_string)
            game.save()
            data['list_of_tries'] = game.try_string.split(',')
            tuple_cowsbulls = check_try(game.answer, player_try)
            if tuple_cowsbulls[1] == '4':
                data['answer'] = f"Вы вычислили загаданное число - {game.answer}. Поздравляем"
                game.delete()
    return render(request, 'game/bullscows.html', context=data)
