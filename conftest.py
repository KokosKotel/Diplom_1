import pytest
from praktikum.burger import Burger
from data import MockBun


@pytest.fixture
def burger():
    burger = Burger()
    burger.set_buns(MockBun.mock_bun)
    return burger
