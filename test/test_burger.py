import pytest
from unittest.mock import Mock


class MockBun:
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Краторная булка"
    mock_bun.get_price.return_value = 1255


class MockIngredientFilling:
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_name.return_value = "Говяжий метеорит"
    mock_ingredient_filling.get_price.return_value = 3000
    mock_ingredient_filling.get_type.return_value = "FILLING"


class MockIngredientSauce:
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_name.return_value = "Соус Spicy-X"
    mock_ingredient_sauce.get_price.return_value = 90
    mock_ingredient_sauce.get_type.return_value = "SAUCE"


class TestBurger:
    def test_burger_set_bun(self, burger):
        assert burger.get_price() == 2510

    @pytest.mark.parametrize("ingredient, total_price",
                             [[MockIngredientSauce.mock_ingredient_sauce, 2600],
                              [MockIngredientFilling.mock_ingredient_filling, 5510]])
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
        assert "(==== Краторная булка ====)" in receipt
        assert "= filling Говяжий метеорит =" in receipt
