def make_sandwich(*toppings):
    print("\nMaking sandwich with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('a')
make_sandwich('a', 'b')
make_sandwich('a', 'b', 'c')
