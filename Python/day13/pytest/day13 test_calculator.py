import calculator

def test_add():
    assert calculator.add(2,3) == 5

def test_subtract():
    assert calculator.subtract(5,3) == 2

def test_mul():
    assert calculator.mul(3,4) == 10