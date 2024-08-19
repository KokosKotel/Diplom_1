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


class ReceiptBurger:
    receipt_burger = (
        "(==== Краторная булка ====)\n"
        "= filling Говяжий метеорит =\n"
        "(==== Краторная булка ====)\n"
        "\n"
        "Price: 5510"
    )
