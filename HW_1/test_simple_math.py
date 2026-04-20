import pytest
from simple_math import SimpleMath


# Фикстура для создания объекта класса

@pytest.fixture
def math_obj():
    return SimpleMath()

# Тесты для square

def test_square_positive(math_obj):
    assert math_obj.square(2) == 4


def test_square_negative(math_obj):
    assert math_obj.square(-2) == 4


def test_square_zero(math_obj):
    assert math_obj.square(0) == 0


# Тесты для cube

def test_cube_positive(math_obj):
    assert math_obj.cube(3) == 27


def test_cube_negative(math_obj):
    assert math_obj.cube(-3) == -27


def test_cube_zero(math_obj):
    assert math_obj.cube(0) == 0