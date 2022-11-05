import pytest

from game.utils import check_try, get_try_string


@pytest.mark.parametrize(
    ('answer', 'player_try', 'try_string', 'result'),
    (
            ("1234", "5678", '', "5678  0:0"),
            ("1234", "1248", "5678  0:0", "5678  0:0,1248  3:2"),
            ("1234", "1234", "5678  0:0,1248  3:2", "5678  0:0,1248  3:2,1234  4:4")
    )
)
def test_get_try_string(answer, player_try, try_string, result):
    test_string = get_try_string(answer, player_try, try_string)
    assert test_string == result
