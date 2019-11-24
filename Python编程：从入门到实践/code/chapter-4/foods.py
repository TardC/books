my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favarite foods are:")
print(my_foods)
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_foods)
for friend_food in friend_foods:
    print(friend_food)
