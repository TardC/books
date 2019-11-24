sandwich_orders = ['tuna', 'cheese', 'apple']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print("I made your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
