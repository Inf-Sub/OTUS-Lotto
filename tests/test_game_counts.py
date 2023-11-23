import pytest

from game import Game, WrongCountValue


# def test_game_counts(monkeypatch):
#     def mock_success_game_counts(*args, **kwargs):
#         pass
#
#     monkeypatch.setattr('game.Game.counts', mock_success_game_counts)

@pytest.mark.parametrize(
    'src, exp_result',
    [
        ('2', 2),
        (2, 2),
        (10, 10),
    ]
)
def test_success_game_counts(src, exp_result):
    test_game = Game()
    test_game.counts = src
    assert (test_game.counts == exp_result)


@pytest.mark.parametrize(
    'src, exp_exception',
    [
        ('1', WrongCountValue),
        (1, WrongCountValue),
        (0, WrongCountValue),
        ('test', WrongCountValue),
    ]
)
def test_error_generate_unique_numbers(src, exp_exception):
    """Должно возникнуть исключение."""
    test_game = Game()
    with pytest.raises(exp_exception):
        test_game.counts = src

