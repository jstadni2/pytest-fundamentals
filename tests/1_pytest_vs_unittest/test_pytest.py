from demos.math_operations import add_numbers, MathOperations


# EXAMPLE 1

def test_add_numbers():
    assert add_numbers(5, 10) == 15
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-1, -1) == -2


# EXAMPLE 2

def test_add():
    math_ops = MathOperations()
    assert math_ops.add(5, 10) == 15
    assert math_ops.add(-1, 1) == 0
    assert math_ops.add(-1, -1) == -2


def test_multiply():
    math_ops = MathOperations()
    assert math_ops.multiply(5, 10) == 50
    assert math_ops.multiply(-1, 1) == -1
    assert math_ops.multiply(-1, -1) == 1
