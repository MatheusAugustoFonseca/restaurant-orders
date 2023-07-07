from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():

    lasagna = Dish("lasanha de presunto", 64.70)
    pizza = Dish("pizza", 45.50)
    # dishes = [lasagna, pizza]

    assert lasagna.name == "lasanha de presunto"
    assert lasagna.name != pizza.name
    assert lasagna.price == 64.70

    assert repr(lasagna) == "Dish('lasanha de presunto', R$64.70)"
    assert hash(lasagna) == hash("Dish('lasanha de presunto', R$64.70)")
    assert lasagna == lasagna
    assert lasagna != pizza

    Ingredient_1 = Ingredient('massa de lasanha')
    lasagna.add_ingredient_dependency(Ingredient_1, 1)
    assert lasagna.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
    }
    assert lasagna.get_ingredients() == {Ingredient_1}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("spaghetti", "40")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("spaghetti", -1)
