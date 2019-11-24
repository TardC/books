pizzas = ['a', 'b', 'c']
for pizza in pizzas:
	print("I like " + pizza + " pizza.")
print(pizzas[0] + ", " + pizzas[1] + ", " + pizzas[2] + ", I really like pizza!")

friend_pizzas = pizzas[:]
pizzas.append('e')
friend_pizzas.append('f')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)
