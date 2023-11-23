import pytest

from game import generate_unique_numbers


@pytest.mark.parametrize(
    'src, exp_result',
    [
        ([5, 1, 5], [1, 2, 3, 4, 5]),
        ([0, 1, 5], []),
        ([-5, 1, 5], []),
        ([-5, 0, 0], []),
    ]
)
def test_success_generate_unique_numbers(src, exp_result):
    result = sorted(generate_unique_numbers(*src))
    assert result == exp_result


@pytest.mark.parametrize(
    'src, exp_exception',
    [
        ([5, 1, 1], ValueError),
        ([15, 1, 3], ValueError),
        (['5', 1, 1], TypeError),
        ([15, '1', 3], TypeError),
    ]
)
def test_error_generate_unique_numbers(src, exp_exception):
    """Должно возникнуть исключение."""
    with pytest.raises(exp_exception):
        generate_unique_numbers(*src)
