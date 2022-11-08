# meals = ('yogurt', 'roll', 'steak')
# print(meals[0])

# my_first_empty_dictionary = {}
# my_second_empty_dictionary = dict()

meals = {"breakfast":"yogurt","lunch":"roll", "dinner":"steak"}
# print(meals)

things = {1 : "2", "steve" : [1, 2, 3]}
# print(things)

# print(meals["breakfast"])
# print(meals["dinner"])

# print("brunch`" in meals)

meals["supper"] = "pancakes"
# print(meals)

# del(meals["breakfast"])
# print(meals)

# print(list(meals))
# print(meals.keys())
# print(meals.values())

countries = {
    "uk":{"capital": "london", "population": 1000},
    "germany":{"capital": "berlin", "population": 5000},
}

print(countries["germany"]["population"])