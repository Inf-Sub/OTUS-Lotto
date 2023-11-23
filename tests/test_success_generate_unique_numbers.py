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
    'src',
    [
        ([5, 1, 1]),
        ([15, 1, 3]),
    ]
)
def test_value_error_generate_unique_numbers(src):
    """Должно возникнуть исключение с неправильным значением."""
    with pytest.raises(ValueError):
        generate_unique_numbers(*src)


@pytest.mark.parametrize(
    'src',
    [
        (['5', 1, 1]),
        ([15, '1', 3]),
    ]
)
def test_type_error_generate_unique_numbers(src):
    """Должно возникнуть исключение с неправильным значением."""
    with pytest.raises(TypeError):
        generate_unique_numbers(*src)
