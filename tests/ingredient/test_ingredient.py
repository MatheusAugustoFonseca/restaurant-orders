from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1 iniciando o projeto
def test_ingredient():
    shrimp = Ingredient("camarão")
    cheese = Ingredient("queijo mussarela")

    assert shrimp.__hash__() == shrimp.__hash__()
    assert shrimp.__hash__() != cheese.__hash__()

    assert shrimp.__repr__() == "Ingredient('camarão')"
    assert shrimp.name == "camarão"
    assert Restriction.SEAFOOD in shrimp.restrictions
    assert Restriction.ANIMAL_MEAT in shrimp.restrictions
    assert Restriction.ANIMAL_DERIVED in shrimp.restrictions

    assert shrimp.__eq__(shrimp) is True
