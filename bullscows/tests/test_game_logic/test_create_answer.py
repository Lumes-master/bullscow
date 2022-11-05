import pytest
from random import sample

@pytest.fixture(scope="module")
def create_answer() -> str:
    """create 4number answer with different digits. Used in
    "creating_new_game" function """
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    answer = ''.join(sample(number_list, 4))
    return answer

def test_create_answer_len(create_answer):
    answer = create_answer
    assert len(answer) == 4

def test_create_answer_set(create_answer):
    answer = set(create_answer)
    assert len(answer) == 4

def test_create_answer_digits(create_answer):
    answer = create_answer
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    assert all(map(lambda x: x in number_list, answer))
