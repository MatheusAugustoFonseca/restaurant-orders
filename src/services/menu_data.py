import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        # pass
        self.dishes = set()
        with open(source_path) as csv_file:
            data = csv.DictReader(csv_file)
            list_dishes = {}

            for row in data:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_qnt = int(row["recipe_amount"])
                ingredient = Ingredient(ingredient_name)
                dish = list_dishes.get(dish_name)

                if dish is None:
                    dish = Dish(dish_name, dish_price)
                    list_dishes[dish_name] = dish
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, ingredient_qnt)
