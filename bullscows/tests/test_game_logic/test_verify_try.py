import pytest


# def verify_try(player_try: str) -> bool:
#     """Validating player try-number Used in "game logic" function """
#     if len(player_try) == 4 and len(set(player_try)) == 4:
#         for i in player_try:
#             if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
#                 return False
#         return True
#     return False
from game.utils import verify_try


@pytest.mark.parametrize(
    ("player_try", "expected"),
    (
            ("1234", True),
            ("1123", False),
            ("12345", False),
            ("123", False),
            ("0123", False),
            ("12o4", False),
            ("9876", True)
    )
)
def test_verify_try_good(player_try, expected):

    assert verify_try(player_try) == expected