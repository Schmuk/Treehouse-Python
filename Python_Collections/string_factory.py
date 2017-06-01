# Example:
# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# string_factory(values)
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]

template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(values):
    list_of_strings = []
    for item in values:
        list_of_strings.append(template.format(**item))
    return list_of_strings

# print(string_factory(values))