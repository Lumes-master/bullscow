"""Functions for game logic """
from random import sample

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

def check_try(answer: str, player_try: str) ->tuple:
    bulls=0
    cows = 0
    for i in range(len(player_try)):
        if player_try[i] == answer[i]:
            cows+=1
            bulls+=1
        elif player_try[i] in answer:
            cows+=1
    return str(cows), str(bulls)

def get_try_string(answer: str, player_try: str, try_string: str=None) -> str:
    tuple_cowsbulls = check_try(answer, player_try)
    if not try_string:
        try_string = f'{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
        return try_string
    else:
        try_string += f',{player_try}  {tuple_cowsbulls[0]}:{tuple_cowsbulls[1]}'
    return  try_string




if __name__ == '__main__':
    a = create_answer()
    print(a)
    try_string = ""
    player_try = "5678"
    try_string= get_try_string(a, player_try, try_string)
    print(try_string)
    player_try1 = "3456"
    try_string = get_try_string(a, player_try1, try_string)
    print(try_string)
    try_list = try_string.split(',')
    print(try_list)


