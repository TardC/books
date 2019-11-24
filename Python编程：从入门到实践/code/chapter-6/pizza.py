# Store you ordered pizza's information
pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize you ordered pizza
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
