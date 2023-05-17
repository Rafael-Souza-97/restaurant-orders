from src.models.dish import Dish, Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as restaurant_file_csv:
            restaurant_data = csv.DictReader(restaurant_file_csv)
            all_dishes = {}

            for row in restaurant_data:
                dish = row["dish"]
                recipe_price = float(row["price"])
                recipe_ingredient = Ingredient(row["ingredient"])
                recipe_amount = int(row["recipe_amount"])

                if dish not in all_dishes:
                    all_dishes[dish] = Dish(dish, recipe_price)

                all_dishes[dish].add_ingredient_dependency(
                    recipe_ingredient, recipe_amount
                    )

                self.dishes = set(all_dishes.values())
