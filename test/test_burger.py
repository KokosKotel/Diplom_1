import pytest

from data import MockBun, MockIngredientFilling, MockIngredientSauce, ReceiptBurger


class TestBurger:
    def test_burger_set_bun(self, burger):
        burger.set_buns(MockBun.mock_bun)
        assert burger.get_price() == 2510

    @pytest.mark.parametrize("ingredient, total_price",
                             [
                                 (MockIngredientFilling.mock_ingredient_filling, 5510),
                                 (MockIngredientSauce.mock_ingredient_sauce, 2600)
                             ])
    def test_burger_add_ingredient(self, burger, ingredient, total_price):
        burger.add_ingredient(ingredient)
        assert burger.get_price() == total_price

    def test_burger_remove_ingredient(self, burger):
        burger.add_ingredient(MockIngredientSauce.mock_ingredient_sauce)
        burger.remove_ingredient(0)
        assert burger.get_price() == 2510

    def test_burger_move_ingredient(self, burger):
        burger.add_ingredient(MockIngredientSauce.mock_ingredient_sauce)
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        burger.move_ingredient(1, 2)
        assert burger.get_price() == 5600

    def test_burger_get_receipt(self, burger):
        burger.add_ingredient(MockIngredientFilling.mock_ingredient_filling)
        receipt = burger.get_receipt()
        assert receipt == ReceiptBurger.receipt_burger
