import pytest

from game import Card


@pytest.mark.parametrize(
    'src, exp_exception',
    [
        ('50', ValueError),
        (-1, ValueError),
        (91, ValueError),
        (100, ValueError),
    ]
)
def test_success_card_cross_num_raises(src, exp_exception):
    test_card = Card()
    with pytest.raises(exp_exception):
        test_card.cross_num(src)

