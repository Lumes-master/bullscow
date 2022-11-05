import pytest


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

@pytest.mark.parametrize(
    ("answer", "player_try", "result"),
    (
        ("1234", "5678", ("0","0")),
        ("1234", "1248", ("3","2")),
        ("1234", "1234", ("4","4"))
    )
)
def test_check_try(answer, player_try, result):
    assert check_try(answer, player_try) == result