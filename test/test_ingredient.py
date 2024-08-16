from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient("FILLING", "Мини-салат Экзо-Плантаго", 4400)
        assert ingredient.get_name() == "Мини-салат Экзо-Плантаго", "Неправильное название начинки"

    def test_ingredient_get_price(self):
        ingredient = Ingredient("FILLING", "Мини-салат Экзо-Плантаго", 4400)
        assert ingredient.get_price() == 4400, "Неправильная цена начинки"

    def test_ingredient_get_type(self):
        ingredient = Ingredient("FILLING", "Мини-салат Экзо-Плантаго", 4400)
        assert ingredient.get_type() == "FILLING", "Неправильный тип начинки"
