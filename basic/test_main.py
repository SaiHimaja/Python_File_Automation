from main import add,divide
import pytest

def test_add():
    assert add(10,20) ==30
    assert add(-1, 1)==0
    assert add(0,0)==0


def test_divide():
    assert divide(6,2) == 3
    with pytest.raises(ValueError,match = "Cannot divide by zero"):
        divide(10,0)
    assert divide(10,2)==5
        