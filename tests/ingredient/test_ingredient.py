from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    mozzarella_ingredient = Ingredient("queijo mussarela")
    assert mozzarella_ingredient.name == "queijo mussarela"
    assert mozzarella_ingredient.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
    assert mozzarella_ingredient.__eq__(Ingredient("queijo mussarela"))
    assert mozzarella_ingredient.__eq__(Ingredient("ovo")) is False
    assert hash(mozzarella_ingredient) == hash("queijo mussarela")
    assert hash(mozzarella_ingredient) != hash(Ingredient("ovo"))
    assert mozzarella_ingredient.__repr__() == "Ingredient('queijo mussarela')"

    flour_ingredient = Ingredient("farinha")
    assert flour_ingredient.name == "farinha"
    assert flour_ingredient.restrictions == {Restriction.GLUTEN}
    assert flour_ingredient.__eq__(Ingredient("farinha"))
    assert flour_ingredient.__eq__(Ingredient("ovo")) is False
    assert hash(flour_ingredient) == hash("farinha")
    assert hash(flour_ingredient) != hash(Ingredient("ovo"))
    assert flour_ingredient.__repr__() == "Ingredient('farinha')"

    salt_ingredient = Ingredient("sal")
    assert salt_ingredient.name == "sal"
    assert salt_ingredient.__eq__(Ingredient("sal"))
    assert salt_ingredient.__eq__(Ingredient("ovo")) is False
    assert hash(salt_ingredient) == hash("sal")
    assert hash(salt_ingredient) != hash(Ingredient("ovo"))
    assert salt_ingredient.__repr__() == "Ingredient('sal')"
