import pytest

from contextlib import nullcontext as does_not_raise
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
    'src, exp_result, expectation',
    [
        ([7, 1, 7], [1, 2, 3, 4, 5, 6, 7], does_not_raise()),
        ([0, 1, 5], [], does_not_raise()),
        ([5, 1, 1], [], pytest.raises(ValueError)),
        ([5, 1, 1], [], pytest.raises(ValueError)),
        ([15, 1, 3], [], pytest.raises(ValueError)),
        (['5', 1, 1], [], pytest.raises(TypeError)),
        ([15, '1', 3], [], pytest.raises(TypeError)),
    ]
)
def test_error_generate_unique_numbers(src, exp_result, expectation):
    """Должно возникнуть исключение."""
    with expectation:
        result = sorted(generate_unique_numbers(*src))
        assert result == exp_result
