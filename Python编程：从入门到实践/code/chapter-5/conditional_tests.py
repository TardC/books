car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True." )
print(fruit == 'apple')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

food = 'cookie'
print("\nIs food == 'cookie'? I predict True.")
print(food == 'cookie')

print("\nIs food == 'burger'? I predict False.")
print(food == 'burger')

answer = 'yes'
print("\nIs answer == 'yes'? I predict True.")
print(answer == 'yes')

print("\nIs answer == 'no'? I predict False.")
print(answer == 'no')

number = 1
print("\nIs number == 1? I predict True.")
print(number == 1)

print("\nIs number == 2? I predict False.")
print(number == 2)


string_1 = 'hello'
string_2 = 'hello'
print("\nstring_1 == string_2?")
print(string_1 == string_2)

string_1 = 'hello'
string_2 = 'world'
print("\nstring_1 == string_2?")
print(string_1 == string_2)

greeting = 'Hello world'
print("\ngreeting == 'hello world'?")
print(greeting.lower() == 'hello world')

print("\ngreeting == 'hello world'?")
print(greeting == 'hello world')

number_1 = 0
number_2 = 1
print("\nnumber_1 == number_2?")
print(number_1 == number_2)

print("\nnumber_1 != number_2?")
print(number_1 != number_2)

print("\nnumber_1 > number_2?")
print(number_1 > number_2)

print("\nnumber_1 < number_2?")
print(number_1 < number_2)

print("\nnumber_1 >= number_2")
print(number_1 >= number_2)

print("\nnumber_1 <= number_2")
print(number_1 <= number_2)

print("\nBoth number_1 and number_2 >= 1?")
print((number_1 >= 1) and (number_2 >= 1))

print("\nEither number_1 or number_2 >= 1?")
print((number >= 1) or (number_2 >= 1))

fruits = ['apple', 'banana', 'orange']
print("\n'apple' in fruits?")
print('apple' in fruits)

print("\n'watermelon' in fruits?")
print('watermelon' in fruits)

print("\n'apple' not in fruits?")
print('apple' not in fruits)

print("\n'watermelon' not in fruits")
print('watermelon' not in fruits)

fruit = 'apple'

if fruit in fruits:
    print("\nI like eat " + fruit + '.' )

fruit = 'watermelon'

if fruit not in fruits:
    print("\nI want " + fruit + '.')
